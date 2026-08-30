
**List of LLM Concepts Overview:-**

GPT, Claude, Gemini, and LLaMA → Transformer-based (decoder-only or variants with attention optimizations). Mamba, S4 → State Space Models (SSM) using linear-time sequence modeling instead of attention.
xLSTM, RWKV → RNN-style or hybrid architectures combining recurrence with transformer-like capabilities.

<img width="701" height="889" alt="image" src="https://github.com/user-attachments/assets/8e0533d2-27bc-48db-858e-8abd2b5ab8fa" />


**Context Window** is the maximum number of tokens an LLM can process at once. Context window is the fixed-length token buffer (size N) that a Transformer attends over during inference/training.
Self-attention computes interactions across all tokens within this window, giving O(N²) time/memory complexity.
Tokens beyond N are dropped or require techniques like sliding windows, chunking, or extended-context methods (e.g., RoPE scaling).

<img width="478" height="327" alt="image" src="https://github.com/user-attachments/assets/2adad8cc-96b2-48f6-b68d-bac6ee429162" />

    4K → short conversations (~3 pages)
    32K → long docs (~20 pages)
    128K → books / codebases
    1M → entire repositories or multiple PDFs


**List of LLMs Summary Evaluation Methods :-**

<img width="1508" height="346" alt="image" src="https://github.com/user-attachments/assets/3dae0071-8d59-42f6-8159-531478fb8294" />


**Mover Score :-**

Measure minimum "cost" to move word embeddings from candidate to reference using Earth Mover’s Distance (Optimal Transport).

MoverScore computes distances between every candidate and reference token embedding.
The distance usually uses Euclidean norm between embeddings.
Smaller distances indicate stronger semantic similarity.


**BERT Score :-** 

Measure semantic similarity between candidate summary and reference using contextual embeddings (e.g., BERT).


