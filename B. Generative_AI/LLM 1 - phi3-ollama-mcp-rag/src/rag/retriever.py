from __future__ import annotations

from src.rag.ingest import _collection, _embed
from src.rag.settings import settings


def retrieve(question: str, top_k: int | None = None) -> list[dict]:
    k = top_k or settings.top_k

    res = _collection.query(
        query_embeddings=[_embed(question)],
        n_results=k,
        include=["documents", "metadatas", "distances"],
    )

    docs = res.get("documents", [[]])[0]
    metas = res.get("metadatas", [[]])[0]
    dists = res.get("distances", [[]])[0]
    ids = res.get("ids", [[]])[0] if "ids" in res else [None] * len(docs)

    return [
        {
            "id": ids[i],
            "text": docs[i],
            "metadata": metas[i] if i < len(metas) else {},
            "distance": dists[i] if i < len(dists) else None,
        }
        for i in range(len(docs))
    ]


def list_sources() -> list[str]:
    data = _collection.get(include=["metadatas"])
    metadatas = data.get("metadatas", []) or []

    sources = sorted(
        {
            meta.get("source")
            for meta in metadatas
            if isinstance(meta, dict) and meta.get("source")
        }
    )

    return sources