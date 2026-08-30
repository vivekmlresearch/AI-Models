from __future__ import annotations

from dataclasses import dataclass

from transformers import AutoModelForSequenceClassification, AutoTokenizer

@dataclass
class DebertaConfig:
    model_name: str = "microsoft/deberta-v3-base"
    num_labels: int = 3
    max_length: int = 1024

def build_tokenizer(config: DebertaConfig):
    return AutoTokenizer.from_pretrained(
        config.model_name,
        use_fast=False,
    )


def build_model(model_name: str, num_labels: int):
    return AutoModelForSequenceClassification.from_pretrained(
        model_name,
        num_labels=num_labels,
    )