from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Ollama configuration
    ollama_base_url: str = "http://ollama:11434"
    ollama_model: str = "phi3:mini"   # lighter model

    # Embedding model (already lightweight and good)
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