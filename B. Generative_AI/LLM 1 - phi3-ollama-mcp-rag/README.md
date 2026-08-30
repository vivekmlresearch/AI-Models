# MCP-RAG Assistant (Containerized)

Local RAG with:
- Ollama (Llama 3.1 8B)
- Chroma vector store
- MCP-style tool server exposing retrieval tools
- FastAPI `/ask` endpoint returning answers with citations
- phi3:mini 

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


## Architecture

<img width="338" height="767" alt="image" src="https://github.com/user-attachments/assets/701b8e62-5611-4a22-a83e-6c7e027213ad" />



##  RAG Flow

      1. src/rag/ingest.py → reads files from data/ folder
      2. It uses iter_text_files() → finds .txt and .md files
      3. Then read_text() → loads file content
      4. Then simple_chunk() (chunking.py) → splits text into chunks
      5. Then embeddings are created using SentenceTransformer
      6. Finally stored in ChromaDB collection (vector database)
      7. If data/ is empty → nothing is ingested → retrieval returns empty → LLM gets no context
      8. Stored location → CHROMA_DIR=/app/.chroma inside container
      9. Format → NOT files → stored as vector embeddings + metadata + text
      10. Each chunk = {id, text, embedding, metadata} in ChromaDB


# Hosting

1. Local Hosting, 2. Cloud Hosting

1.Local Hosting

   <img width="1767" height="417" alt="image" src="https://github.com/user-attachments/assets/a4be81e1-1618-4f23-9ee5-7b7b09dc9823" />


   While Running:-

   <img width="1277" height="883" alt="image" src="https://github.com/user-attachments/assets/087a28e9-14a0-41d9-8082-7f49d62369b6" />


   Question 1:-
   
<img width="732" height="111" alt="image" src="https://github.com/user-attachments/assets/b806037e-95c0-49a0-8b6d-d9553ec437f9" />


   Response 1:-

   <img width="1742" height="762" alt="image" src="https://github.com/user-attachments/assets/0986a709-9f60-46a4-a6ef-47162d290bac" />




# Evaluation Metrics

1. Hallucination Rate (Groundedness) – % of claims not supported by retrieved context → measured via claim verification or LLM judge

2. Answer Accuracy (EM/F1/LLM score) – correctness vs ground truth → exact match, F1, or model-based scoring

3. Retrieval Recall@k – whether relevant documents are retrieved → relevant_docs_retrieved / total_relevant_docs

4. Citation Accuracy (Attribution Score) – correctness of source references → correct_citations / total_citations

5. Latency (P95/P99) – tail response time → 95th/99th percentile of response time

6. Failure Rate (Error Rate) – % failed or empty responses → failures / total_requests

7. Throughput (RPS) – system capacity → requests per second

8. Cost per Request – token + compute cost → (input + output tokens) × cost/token

9. Context Efficiency (Utilization Ratio) – useful vs total context → relevant_tokens / total_context_tokens

10. User Satisfaction (Engagement Metrics) – user behavior signals → like/dislike rate, retries, drop-offs

## Additional Metrics:-

        1. Total response time
        2. LLM inference time
        3. Retrieval time
        4. Embedding time
        5. Tokens in prompt
        6. Tokens in output
        7. Chunks retrieved
        8. Average chunk relevance score / distance
        9. Context length used
        10. Answer confidence proxy (based on retrieval similarity / citations coverage)




## Notes

This repo is intentionally minimal and lightweight execution friendly. Further to be extended with:
- Hybrid retrieval (BM25 + vectors)
- Reranking
- Eval harness + prompt regression tests
- Proper MCP protocol bindings (depending on MCP host)
