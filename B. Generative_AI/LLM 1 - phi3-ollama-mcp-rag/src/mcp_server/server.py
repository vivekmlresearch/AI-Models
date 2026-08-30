from __future__ import annotations

from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

from .tools import tool_search_documents, tool_list_sources, tool_get_snippets

app = FastAPI(title="MCP Tool Server (Demo)")

class SearchReq(BaseModel):
    query: str
    top_k: int = 6

class SnippetReq(BaseModel):
    ids: list[str]

@app.get("/health")
def health():
    return {"ok": True}

@app.post("/tools/search_documents")
def search_documents(req: SearchReq):
    return tool_search_documents(req.query, req.top_k)

@app.get("/tools/list_sources")
def list_sources():
    return tool_list_sources()

@app.post("/tools/get_snippets")
def get_snippets(req: SnippetReq):
    return tool_get_snippets(req.ids)

if __name__ == "__main__":
    uvicorn.run("src.mcp_server.server:app", host="0.0.0.0", port=8765, reload=False)
