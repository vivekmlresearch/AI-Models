from pathlib import Path
import joblib
import yaml


def load_yaml(path: str) -> dict:
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def ensure_parent(path: str) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)


def save_joblib(obj, path: str) -> None:
    ensure_parent(path)
    joblib.dump(obj, path)


def load_joblib(path: str):
    return joblib.load(path)
