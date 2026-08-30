from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # Ollama configuration
    ollama_base_url: str = "http://ollama:11434"
    ollama_model: str = "phi3:mini"

    # Embedding model
    embedding_model: str = "BAAI/bge-small-en-v1.5"

    # Chroma vector database
    chroma_dir: str = "/app/.chroma"
    chroma_collection: str = "docs"

    # Retrieval settings
    top_k: int = 6
    max_context_chars: int = 8000


settings = Settings()

# docker compose down
# docker system prune -f
# docker compose build --no-cache
# docker compose up

# cd LLM-mcp-rag-assistant

# Situation	Command
# First run	docker compose up --build
# Normal run	docker compose up -d

# Stop	docker compose down
# Debug logs	docker compose logs
# Fix broken build	--no-cache


# http://localhost:8000/docs


# Remove everything
# Docker system prune -a --volumes -f

#docker builder prune -a -f

# docker image prune -a
