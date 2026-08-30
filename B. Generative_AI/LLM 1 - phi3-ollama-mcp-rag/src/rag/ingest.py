from __future__ import annotations

from pathlib import Path
from typing import Iterable

import chromadb
from sentence_transformers import SentenceTransformer

#pip install pypdf
from pypdf import PdfReader

from .chunking import simple_chunk
from .settings import settings


_client = chromadb.PersistentClient(path=settings.chroma_dir)
_collection = _client.get_or_create_collection(settings.chroma_collection)
_embedder = SentenceTransformer(settings.embedding_model)


def _embed(text: str) -> list[float]:
    return _embedder.encode(text, normalize_embeddings=True).tolist()


def iter_text_files(folder: str) -> Iterable[Path]:
    p = Path(folder)
    for ext in ("*.md", "*.txt", "*.pdf"):
        yield from p.rglob(ext)

def read_text(path: Path) -> str:
    if path.suffix == ".pdf":
        reader = PdfReader(str(path))
        return "\n".join([page.extract_text() or "" for page in reader.pages])
    return path.read_text(encoding="utf-8", errors="ignore")


def ingest(folder: str) -> dict:
    docs_added = 0
    chunks_added = 0

    for fp in iter_text_files(folder):
        raw = read_text(fp)
        chunks = simple_chunk(raw)
        if not chunks:
            continue

        ids = []
        metadatas = []
        for i, ch in enumerate(chunks):
            ids.append(f"{fp.name}::chunk::{i}")
            metadatas.append(
                {
                    "source": fp.name,
                    "chunk_id": i,
                    "path": str(fp),
                }
            )

        embeddings = _embedder.encode(chunks, normalize_embeddings=True).tolist()

        _collection.add(
            ids=ids,
            documents=chunks,
            metadatas=metadatas,
            embeddings=embeddings,
        )

        docs_added += 1
        chunks_added += len(chunks)

    return {
        "docs_added": docs_added,
        "chunks_added": chunks_added,
        "folder": folder,
    }