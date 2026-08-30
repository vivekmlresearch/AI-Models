from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import yaml
from datasets import Dataset
from sklearn.metrics import log_loss
from sklearn.model_selection import train_test_split
from transformers import (
    AutoTokenizer,
    DataCollatorWithPadding,
    Trainer,
    TrainingArguments,
    set_seed,
)

from src.data.dataset import CLASS_NAMES, get_targets, read_csv
from src.data.features import build_text
from src.models.deberta import build_model


def load_config(config_path: str) -> dict:
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def clean_text(text: str) -> str:
    if not isinstance(text, str):
        return ""
    # Remove invalid unicode characters
    return text.encode("utf-8", "ignore").decode("utf-8", "ignore")


def build_texts(df):
    return df.apply(
        lambda row: clean_text(
            build_text(
                row["prompt"],
                row["response_a"],
                row["response_b"],
            )
        ),
        axis=1,
    ).tolist()


def compute_metrics(eval_pred):
    logits, labels = eval_pred
    probs = softmax_numpy(logits)
    loss = log_loss(labels, probs, labels=list(range(len(CLASS_NAMES))))
    preds = np.argmax(probs, axis=1)
    acc = float((preds == labels).mean())
    return {
        "log_loss": float(loss),
        "accuracy": acc,
    }


def softmax_numpy(logits: np.ndarray) -> np.ndarray:
    logits = np.asarray(logits)
    shifted = logits - np.max(logits, axis=1, keepdims=True)
    exp_vals = np.exp(shifted)
    return exp_vals / exp_vals.sum(axis=1, keepdims=True)


def tokenize_dataset(dataset: Dataset, tokenizer, max_length: int) -> Dataset:
    def _tokenize(batch):
        return tokenizer(
            batch["text"],
            truncation=True,
            max_length=max_length,
            padding=False,
        )

    return dataset.map(_tokenize, batched=True)


def main(config_path: str) -> None:
    config = load_config(config_path)

    seed = int(config["model"].get("random_state", 42))
    set_seed(seed)

    train_csv = config["paths"]["train_csv"]
    output_dir = Path(config["paths"]["model_dir"])
    output_dir.mkdir(parents=True, exist_ok=True)

    train_df = read_csv(train_csv)
    train_df = train_df.copy()
    
    
    train_df = train_df.sample(2000, random_state=42)

    train_df["label"] = get_targets(train_df)
    train_df["text"] = build_texts(train_df)

    train_split, valid_split = train_test_split(
        train_df[["text", "label"]],
        test_size=float(config["model"].get("valid_size", 0.1)),
        random_state=seed,
        stratify=train_df["label"],
    )

    model_name = config["model"]["pretrained_model_name"]
    max_length = int(config["model"].get("max_length", 512))

    tokenizer = AutoTokenizer.from_pretrained(model_name, use_fast=False)
    model = build_model(model_name=model_name, num_labels=len(CLASS_NAMES))

    train_ds = Dataset.from_dict({
        "text": train_split["text"].tolist(),
        "label": train_split["label"].tolist(),
    })

    valid_ds = Dataset.from_dict({
        "text": valid_split["text"].tolist(),
        "label": valid_split["label"].tolist(),
    })


    train_ds = tokenize_dataset(train_ds, tokenizer, max_length)
    valid_ds = tokenize_dataset(valid_ds, tokenizer, max_length)

    columns_to_keep = ["input_ids", "attention_mask", "label"]
    if "token_type_ids" in train_ds.column_names:
        columns_to_keep.append("token_type_ids")

    train_ds = train_ds.remove_columns([c for c in train_ds.column_names if c not in columns_to_keep])
    valid_ds = valid_ds.remove_columns([c for c in valid_ds.column_names if c not in columns_to_keep])

    data_collator = DataCollatorWithPadding(tokenizer=tokenizer)

    args = TrainingArguments(
        output_dir=str(output_dir),
        learning_rate=float(config["model"].get("learning_rate", 2e-5)),
        per_device_train_batch_size=int(config["model"].get("train_batch_size", 2)),
        per_device_eval_batch_size=int(config["model"].get("eval_batch_size", 2)),
        gradient_accumulation_steps=int(config["model"].get("gradient_accumulation_steps", 1)),
        num_train_epochs=float(config["model"].get("num_train_epochs", 1)),
        weight_decay=float(config["model"].get("weight_decay", 0.01)),
        warmup_ratio=float(config["model"].get("warmup_ratio", 0.0)),
        logging_steps=int(config["model"].get("logging_steps", 10)),
        eval_strategy=config["model"].get("eval_strategy", "epoch"),
        save_strategy=config["model"].get("save_strategy", "epoch"),
        save_total_limit=int(config["model"].get("save_total_limit", 1)),
        load_best_model_at_end=True,
        metric_for_best_model="eval_log_loss",
        greater_is_better=False,
        fp16=bool(config["model"].get("fp16", False)),
        report_to="none",
    )

    trainer = Trainer(
        model=model,
        args=args,
        train_dataset=train_ds,
        eval_dataset=valid_ds,
        data_collator=data_collator,
        compute_metrics=compute_metrics,
    )
    
    trainer.train()

    eval_metrics = trainer.evaluate()
    print("Validation metrics:")
    print(json.dumps(eval_metrics, indent=2))

    trainer.save_model(str(output_dir))
    tokenizer.save_pretrained(str(output_dir))

    metrics_path = output_dir / "metrics.json"
    with open(metrics_path, "w", encoding="utf-8") as f:
        json.dump(eval_metrics, f, indent=2)

    label_map_path = output_dir / "label_mapping.json"
    label_mapping = {idx: name for idx, name in enumerate(CLASS_NAMES)}
    with open(label_map_path, "w", encoding="utf-8") as f:
        json.dump(label_mapping, f, indent=2)

    print(f"Saved model and tokenizer to: {output_dir}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True, help="Path to YAML config")
    args = parser.parse_args()
    main(args.config)