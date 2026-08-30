import pandas as pd


def clean_text(value) -> str:
    if value is None:
        return ""
    if isinstance(value, list):
        return " ".join(map(str, value))
    return str(value).replace("\n", " ").strip()


def build_text(df: pd.DataFrame) -> pd.Series:
    prompt = df["prompt"].map(clean_text)
    a = df["response_a"].map(clean_text)
    b = df["response_b"].map(clean_text)

    len_a = a.str.len().fillna(0)
    len_b = b.str.len().fillna(0)
    diff = (len_a - len_b).astype(str)

    return (
        "[PROMPT] " + prompt
        + " [RESPONSE_A] " + a
        + " [RESPONSE_B] " + b
        + " [LEN_DIFF] " + diff
    )
