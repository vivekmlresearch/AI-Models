from __future__ import annotations

import chromadb
from sentence_transformers import SentenceTransformer

from .settings import settings

_client = chromadb.PersistentClient(path=settings.chroma_dir)
_collection = _client.get_or_create_collection(settings.chroma_collection)
_embedder = SentenceTransformer(settings.embedding_model)

def retrieve(query: str, top_k: int | None = None) -> list[dict]:
    k = top_k or settings.top_k
    q_emb = _embedder.encode([query], normalize_embeddings=True).tolist()[0]
    res = _collection.query(
        query_embeddings=[q_emb],
        n_results=k,
        include=["documents", "metadatas", "distances", "ids"],
    )

    out: list[dict] = []
    for i in range(len(res["ids"][0])):
        out.append({
            "id": res["ids"][0][i],
            "text": res["documents"][0][i],
            "metadata": res["metadatas"][0][i],
            "distance": res["distances"][0][i],
        })
    return out

def list_sources(limit: int = 50) -> list[str]:
    res = _collection.get(include=["metadatas"], limit=limit)
    sources = sorted({m.get("source", "unknown") for m in res.get("metadatas", [])})
    return sources
