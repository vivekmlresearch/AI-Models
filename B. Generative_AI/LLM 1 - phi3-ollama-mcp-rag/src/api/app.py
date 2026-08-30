from __future__ import annotations

from fastapi import FastAPI
from pydantic import BaseModel

from src.rag.retriever import retrieve
from src.rag.citations import build_context
from src.rag.generator import generate_answer
from src.rag.settings import settings
from src.rag.ingest import ingest

app = FastAPI(title="MCP-RAG Assistant")


class AskReq(BaseModel):
    question: str
    top_k: int | None = None


@app.on_event("startup")
async def startup_event():
    ingest("/app/data/sample_docs")


@app.get("/health")
def health():
    return {"ok": True}


@app.post("/ask")
async def ask(req: AskReq):
    chunks = retrieve(req.question, top_k=req.top_k)
    context, citations = build_context(chunks, max_chars=settings.max_context_chars)
    answer = await generate_answer(req.question, context=context)
    return {
        "question": req.question,
        "answer": answer,
        "citations": citations,
        "retrieved": [
            {
                "id": c["id"],
                "metadata": c["metadata"],
                "distance": c["distance"],
            }
            for c in chunks
        ],
    }