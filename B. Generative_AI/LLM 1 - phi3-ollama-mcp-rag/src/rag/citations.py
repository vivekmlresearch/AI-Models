from __future__ import annotations

def build_context(chunks: list[dict], max_chars: int) -> tuple[str, list[dict]]:
    context_parts: list[str] = []
    used: list[dict] = []
    total = 0
    for c in chunks:
        tag = f"[{c['metadata'].get('source')}#chunk{c['metadata'].get('chunk_id')}]"
        piece = f"{tag}\n{c['text']}\n"
        if total + len(piece) > max_chars:
            break
        context_parts.append(piece)
        used.append({
            "source": c["metadata"].get("source"),
            "chunk_id": c["metadata"].get("chunk_id"),
            "id": c["id"],
        })
        total += len(piece)
    return "\n".join(context_parts).strip(), used
