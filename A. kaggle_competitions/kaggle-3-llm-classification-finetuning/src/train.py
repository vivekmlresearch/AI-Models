from __future__ import annotations

import argparse
import pandas as pd
from sklearn.metrics import log_loss
from sklearn.model_selection import train_test_split

from src.data.dataset import CLASS_NAMES, TARGET_COLUMNS, get_targets, read_csv
from src.data.features import build_text
from src.models.baseline import BaselineConfig, build_pipeline
from src.utils.io import load_yaml, save_joblib
from src.utils.logger import get_logger
from src.utils.seed import set_seed

logger = get_logger(__name__)


def main(config_path: str) -> None:
    config = load_yaml(config_path)
    set_seed(config["seed"])

    train_df = read_csv(config["paths"]["train_csv"])
    y = get_targets(train_df)
    X = build_text(train_df)

    X_train, X_valid, y_train, y_valid = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=config["seed"],
        stratify=y,
    )

    model_cfg = BaselineConfig(
        max_features=config["model"]["max_features"],
        ngram_range=tuple(config["model"]["ngram_range"]),
        C=config["model"]["C"],
        max_iter=config["model"]["max_iter"],
        random_state=config["seed"],
    )
    model = build_pipeline(model_cfg)
    model.fit(X_train, y_train)

    valid_probs = model.predict_proba(X_valid)
    score = log_loss(y_valid, valid_probs)
    logger.info("Validation log loss: %.6f", score)

    full_model = build_pipeline(model_cfg)
    full_model.fit(X, y)
    save_joblib(full_model, config["paths"]["model_path"])
    logger.info("Saved model to %s", config["paths"]["model_path"])

    oof = pd.DataFrame(valid_probs, columns=TARGET_COLUMNS)
    oof.to_csv(config["paths"]["oof_path"], index=False)
    logger.info("Saved validation predictions to %s", config["paths"]["oof_path"])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    args = parser.parse_args()
    main(args.config)
