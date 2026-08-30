"""
Data ingestion module.
Downloads or loads the heart disease dataset from the configured path.
"""

import pandas as pd
from pathlib import Path
import yaml
from src.utils.logger import get_logger

logger = get_logger(__name__)


def load_config(config_path: str = "configs/config.yaml") -> dict:
    with open(config_path, "r") as f:
        return yaml.safe_load(f)


def load_raw_data(config: dict) -> pd.DataFrame:
    """
    Load raw CSV data from the path specified in config.

    Args:
        config: Parsed config dict

    Returns:
        Raw DataFrame
    """
    raw_path = config["data"]["raw_path"]
    logger.info(f"Loading raw data from: {raw_path}")

    if not Path(raw_path).exists():
        raise FileNotFoundError(
            f"Raw data not found at {raw_path}. "
            "Please download from Kaggle and place at the specified path, "
            "or run `dvc pull` if using DVC remote."
        )

    df = pd.read_csv(raw_path)
    logger.info(f"Loaded dataset: {df.shape[0]} rows, {df.shape[1]} columns")
    return df


if __name__ == "__main__":
    config = load_config()
    df = load_raw_data(config)
    print(df.head())
    print(df.info())
