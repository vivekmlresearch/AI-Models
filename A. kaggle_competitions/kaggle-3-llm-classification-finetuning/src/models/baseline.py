from __future__ import annotations

from dataclasses import dataclass

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline


@dataclass
class BaselineConfig:
    max_features: int = 50000
    ngram_range: tuple[int, int] = (1, 2)
    C: float = 3.0
    max_iter: int = 1200
    random_state: int = 42


def build_pipeline(config: BaselineConfig) -> Pipeline:
    return Pipeline(
        steps=[
            (
                "tfidf",
                TfidfVectorizer(
                    max_features=config.max_features,
                    ngram_range=config.ngram_range,
                    strip_accents="unicode",
                    lowercase=True,
                    sublinear_tf=True,
                    min_df=2,
                ),
            ),
            (
                "clf",
                LogisticRegression(
                    C=config.C,
                    max_iter=config.max_iter,
                    solver="lbfgs",
                    random_state=config.random_state,
                ),
            ),
        ]
    )


# python -m src.train --config configs/config.yaml
# python -m src.predict --config configs/config.yaml
#
#