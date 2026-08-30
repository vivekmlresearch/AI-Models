#!/usr/bin/env bash
set -euo pipefail
python -c "from src.rag.ingest import ingest; print(ingest('data/sample_docs'))"
