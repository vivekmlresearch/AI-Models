from __future__ import annotations

import httpx
from .settings import settings


SYSTEM = """You are a helpful assistant.

Available tools:
- search_documents: search relevant chunks from documents
- list_sources: list all available document sources
- get_snippets: get document snippets

Use ONLY the provided context to answer.
If the answer is not in the context, say you don't know.
Always include citations like [file.md#chunk2].
"""


async def generate_answer(question: str, context: str) -> str:
    prompt = f"""{SYSTEM}

Context:
{context}

Question: {question}

Answer (with citations):"""

    async with httpx.AsyncClient(timeout=300) as client:
        r = await client.post(
            f"{settings.ollama_base_url}/api/generate",
            json={
                "model": settings.ollama_model,
                "prompt": prompt,
                "stream": False,
            },
        )
        r.raise_for_status()
        data = r.json()
        return data.get("response", "").strip()