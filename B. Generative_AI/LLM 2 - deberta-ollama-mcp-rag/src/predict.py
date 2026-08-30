from __future__ import annotations

import argparse
import pandas as pd

from src.data.dataset import TARGET_COLUMNS, read_csv
from src.models.predictor import Predictor
from src.utils.io import load_yaml
from src.utils.logger import get_logger

logger = get_logger(__name__)


def main(config_path: str) -> None:
    config = load_yaml(config_path)
    test_df = read_csv(config["paths"]["test_csv"])
    predictor = Predictor(
        model_dir=config["paths"]["model_dir"],
        max_length=config["model"]["max_length"],
        batch_size=config["model"]["eval_batch_size"],
    )
    probs = predictor.predict_proba(test_df)

    submission = pd.DataFrame(probs, columns=TARGET_COLUMNS)
    submission.insert(0, "id", test_df["id"])
    submission.to_csv(config["paths"]["submission_path"], index=False)
    logger.info("Saved submission to %s", config["paths"]["submission_path"])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    args = parser.parse_args()
    main(args.config)
