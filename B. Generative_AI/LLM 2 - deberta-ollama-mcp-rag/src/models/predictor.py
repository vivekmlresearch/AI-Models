from __future__ import annotations

import numpy as np
import pandas as pd
import torch
from torch.utils.data import DataLoader
from transformers import AutoModelForSequenceClassification, AutoTokenizer, DataCollatorWithPadding

from src.data.features import build_text


class Predictor:
    def __init__(self, model_dir: str, max_length: int = 1024, batch_size: int = 4):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.tokenizer = AutoTokenizer.from_pretrained(model_dir, use_fast=True)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_dir)
        self.model.to(self.device)
        self.model.eval()
        self.max_length = max_length
        self.batch_size = batch_size
        self.collator = DataCollatorWithPadding(tokenizer=self.tokenizer, pad_to_multiple_of=8 if torch.cuda.is_available() else None)

    def _encode(self, texts: list[str]) -> list[dict]:
        encoded = self.tokenizer(
            texts,
            truncation=True,
            max_length=self.max_length,
        )
        items = []
        for i in range(len(texts)):
            items.append({k: v[i] for k, v in encoded.items()})
        return items

    def predict_proba(self, df: pd.DataFrame) -> np.ndarray:
        texts = build_text(df)
        items = self._encode(texts)
        loader = DataLoader(items, batch_size=self.batch_size, shuffle=False, collate_fn=self.collator)

        probs = []
        with torch.no_grad():
            for batch in loader:
                batch = {k: v.to(self.device) for k, v in batch.items()}
                logits = self.model(**batch).logits
                batch_probs = torch.softmax(logits, dim=-1).cpu().numpy()
                probs.append(batch_probs)
        return np.vstack(probs)
