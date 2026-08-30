from __future__ import annotations

import httpx
from .settings import settings

SYSTEM = """You are a helpful assistant.
Use ONLY the provided context to answer.
If the answer is not in the context, say you don't know.
Always include citations in square brackets referencing the context tags, e.g. [file.md#chunk2].
"""

async def generate_answer(question: str, context: str) -> str:
    prompt = f"""Context:
{context}

Question: {question}

Answer (with citations):"""

    async with httpx.AsyncClient(timeout=60) as client:
        r = await client.post(
            f"{settings.ollama_base_url}/api/chat",
            json={
                "model": settings.ollama_model,
                "messages": [
                    {"role": "system", "content": SYSTEM},
                    {"role": "user", "content": prompt},
                ],
                "stream": False,
            },
        )
        r.raise_for_status()
        data = r.json()
        return data["message"]["content"]
