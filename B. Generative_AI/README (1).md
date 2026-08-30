# MCP-RAG Assistant (Containerized)

Local-first RAG with:
- Ollama (Llama 3.1 8B)
- Chroma vector store
- MCP-style tool server exposing retrieval tools
- FastAPI `/ask` endpoint returning answers with citations

## Quickstart

```bash
cp .env.example .env
docker compose up --build -d

# First time only: pull the model inside the ollama container
docker compose exec ollama ollama pull llama3.1:8b

# Ingest sample docs into Chroma
docker compose exec app bash -lc "./scripts/ingest_sample.sh"
```

Ask a question:
```bash
curl -s http://localhost:8000/ask   -H "Content-Type: application/json"   -d '{"question":"What does this repo demonstrate?"}'
```

## Services

- **app** (FastAPI): `http://localhost:8000`
  - `POST /ask`
- **mcp-server** (tool server): `http://localhost:8765`
  - `GET /tools/list_sources`
  - `POST /tools/search_documents`

## Notes

This repo is intentionally minimal and laptop-friendly. Extend it with:
- Hybrid retrieval (BM25 + vectors)
- Reranking
- Eval harness + prompt regression tests
- Proper MCP protocol bindings (depending on your MCP host)
