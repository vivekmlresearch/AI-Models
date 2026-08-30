from __future__ import annotations

from typing import Any
from src.rag.retriever import retrieve, list_sources

def tool_search_documents(query: str, top_k: int = 6) -> dict[str, Any]:
    hits = retrieve(query, top_k=top_k)
    return {"results": hits}

def tool_list_sources() -> dict[str, Any]:
    return {"sources": list_sources()}

def tool_get_snippets(ids: list[str]) -> dict[str, Any]:
    return {"note": "Not implemented in demo; use search_documents for now.", "ids": ids}
