import pandas as pd

from src.data.features import build_text


def test_build_text_returns_series():
    df = pd.DataFrame(
        {
            "prompt": ["hello"],
            "response_a": ["hi"],
            "response_b": ["hey"],
        }
    )
    result = build_text(df)
    assert len(result) == 1
    assert "[PROMPT]" in result.iloc[0]
