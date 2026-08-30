from __future__ import annotations

import ast

def _safe_to_text(value) -> str:
    if value is None:
        return ""
    if isinstance(value, float):
        try:
            if value != value:
                return ""
        except Exception:
            pass
    if isinstance(value, list):
        return "\n".join(str(x) for x in value)
    if isinstance(value, str):
        text = value.strip()
        if not text:
            return ""
        # Some rows may store prompt/response as a stringified list
        if text.startswith("[") and text.endswith("]"):
            try:
                parsed = ast.literal_eval(text)
                if isinstance(parsed, list):
                    return "\n".join(str(x) for x in parsed)
            except Exception:
                pass
        return text
    return str(value)


def build_text(prompt, response_a, response_b) -> str:
    prompt_text = _safe_to_text(prompt)
    a_text = _safe_to_text(response_a)
    b_text = _safe_to_text(response_b)

    return (
        f"Prompt:\n{prompt_text}\n\n"
        f"Response A:\n{a_text}\n\n"
        f"Response B:\n{b_text}"
    )