# Generative AI, LLM and MLops Concepts

This repository is structured with the goal of building a Model-as-a-Service (MaaS) ecosystem. It serves as a comprehensive playground for experimenting, designing, and comparing modern AI/ML architectures.

    A. Model Experiments
    B. MLops Architectures
    C. Architecture Scinarios
    D. Core Concepts & framworks
    E. Architecture Comparisions

**LLM-MCP Combinatory Stacks:**

A curated collection of modern LLM pipelines integrating orchestration frameworks, vector databases, and MCP (Model Context Protocol):

      1. GPT-4o + OpenAI API + LangChain + Pinecone + MCP
      2. Claude 3.5 Sonnet + Anthropic API + LangGraph + Weaviate + MCP
      3. Gemini 1.5 Pro + Vertex AI + BigQuery + MCP
      4. GPT-4 / Phi + Azure OpenAI Service + Azure Cognitive Search + LangChain
      5. Llama 3 70B + vLLM + Milvus + MCP
      6. Phi-3 Mini + Ollama + Chroma + MCP
      7. Mistral 7B + Ollama + Open WebUI + Chroma + MCP
      8. Llama 3 8B + LM Studio + LlamaIndex
      9. Mistral / Phi + llama.cpp + AutoGen + Chroma + MCP
      10. TinyLlama + llama.cpp + FAISS + Haystack

**Enterprise / GPU cluster oriented:-**

Production-grade, scalable stacks designed for enterprise and high-performance environments:

    1. Nemotron + NVIDIA Triton + NeMo + Vector DB + MCP (NVIDIA Stack)
    2. Llama 3 70B + vLLM + Ray Serve + Milvus + MCP (Meta Enterprise Stack)
    3. GPT-4o + Azure OpenAI Service + Azure Kubernetes Service + Azure Cognitive Search + MCP (OpenAI Enterprise-style Stack)
    4. Gemini 1.5 Pro + Vertex AI + Kubernetes + BigQuery + MCP (Google Deep Enterprise Stack)


**Architectural Scinarios**

1. Azure Focused Enterprise Agent:- An enterprise agent built on MCP, PPM, and RAC enables real-time decision-making by integrating structured data from Azure SQL Database and unstructured knowledge indexed in Azure AI Search. It accesses internal documents from SharePoint and OneDrive via MCP connectors, while enriching context through external APIs. Retrieval pipelines combine hybrid and vector search using embeddings stored in Pinecone. Orchestration and execution are handled by Azure Machine Learning with Python-based tools, governed by policy and planning layers. Workflows are triggered via event-driven systems (Event Grid/Service Bus) or scheduled pipelines (Azure ML/ADF), with full MLOps support including CI/CD, model versioning, and monitoring. The agent completes actions through Teams notifications, email automation, and enterprise APIs, enabling end-to-end autonomous operations.
    
2. GCP Focused Enterprise Agent:- An enterprise agent leveraging MCP, PPM, and RAC delivers intelligent automation by connecting structured data from BigQuery and unstructured knowledge through Vertex AI Search. It ingests enterprise content from Google Drive and Google Docs via MCP connectors, while integrating external APIs for dynamic context. RAC pipelines utilize embeddings and semantic retrieval powered by Vertex AI with vector storage options like AlloyDB. Execution and orchestration are managed through Vertex AI with Python-based tools, guided by planning and governance policies. Scheduling is handled via Pub/Sub (event-driven) and Cloud Scheduler/Vertex Pipelines (batch), with MLOps capabilities including CI/CD, model registry, monitoring, and scalable data pipelines. The agent closes the loop Google Chat, Gmail automation, and external APIs for fully autonomous enterprise workflows.

3. AWS Focused Enterprise Agent:- An enterprise agent built on MCP, PPM, and RAC can deliver real-time decision intelligence on AWS by combining structured data in Amazon Aurora/RDS or Amazon Redshift with unstructured enterprise knowledge retrieved through Amazon Bedrock knowledge capabilities and Amazon OpenSearch Service for hybrid and vector search. It can access internal documents from Amazon S3, SharePoint, or OneDrive through MCP-style connectors, enrich context with external web and business APIs, and use Python-based code execution plus orchestration through AWS Step Functions, Lambda, or SageMaker for multi-step reasoning and execution. Scheduling can be handled through Amazon EventBridge for event-driven triggers and time-based automation, while MLOps is supported through model lifecycle management, pipelines, monitoring, logging, and policy enforcement across the stack. The agent closes the loop through action tools such as Teams or Slack notifications, email automation via Amazon SES, and downstream business APIs for fully autonomous enterprise workflows.


**MLOps:-**

        1. Data Versioning: Tracking changes in datasets over time to ensure reproducibility and consistency across experiments.
        2. Model Versioning: Managing different versions of models (training runs, hyperparameters, artifacts) for traceability and rollback.
        3. Experiment Tracking: Logging metrics, parameters, and results of experiments using tools like MLflow to compare performance.
        4. CI/CD for ML: Automating the build, test, and deployment of ML pipelines and models using tools like GitHub Actions or Jenkins.
        5. Feature Engineering & Feature Store: Creating, storing, and serving features consistently for both training and inference.
        6. Pipeline Orchestration: Automating workflows (data ingestion → training → deployment) using tools like Apache Airflow or Kubeflow.
        7. Model Deployment: Serving models via APIs, batch jobs, or streaming systems using scalable infrastructure.
        8. Monitoring & Observability: Tracking model performance, latency, drift, and failures in production.
        9. Model Drift & Data Drift Detection: Identifying when model accuracy degrades due to changing data distributions.
        10. Governance & Compliance: Ensuring models follow policies, explainability, security, and regulatory requirements.
        11. Automated Retraining: Triggering model retraining based on drift, performance drop, or scheduled intervals.
        12. Feature Drift Monitoring: Tracking changes in input feature distributions over time.
        13. Canary Deployment: Gradually rolling out a new model to a small subset of users before full deployment.
        14. Shadow Deployment: Running a new model alongside the existing one without affecting users to evaluate performance.
        15. Infrastructure as Code (IaC): Managing infrastructure (compute, storage, pipelines) using code (e.g., Terraform).
        16. Security & Access Control: Managing permissions, and secure data/model access across systems.
        17. Model Registry:- Stores, versions, and manages models across environments

**Model Optimization:-**

        1. Quantization → Reduces precision (e.g., FP32 → INT8) to improve speed and reduce memory

                **Types:-**
                Post-Training Quantization (PTQ) – applied after training, no retraining needed
                Quantization-Aware Training (QAT) – simulated during training for better accuracy
                Dynamic Quantization – quantizes weights, activations at runtime
                Static Quantization – quantizes weights + activations using calibration data
                Weight-only Quantization – compresses only model weights
                Integer Quantization (INT8/INT4) – reduces precision for efficiency
                Float Quantization (FP16/BF16) – lower precision floating-point
                Per-Tensor Quantization – single scale for entire tensor
                Per-Channel Quantization – different scales per channel (more accurate)
                LLM-specific (GPTQ, AWQ, SmoothQuant) – optimized for large language models


                **Formats**
                FP32 (Float32) – Full precision (baseline, no quantization)
                FP16 (Float16) – Half precision, widely used on GPUs
                BF16 (BFloat16) – Better range than FP16, used in training
                INT8 – Most common quantized format (good balance of speed & accuracy)
                INT4 – Lower precision, high compression (used in LLMs)
                INT2 – Extremely compressed, experimental
                UINT8 – Unsigned 8-bit (used in some hardware accelerators)
                Binary (1-bit) – Weights as 0/1 (very aggressive compression)
                Ternary (2-bit) – Values like {-1, 0, 1}
                Mixed Precision (FP16 + INT8) – Combination for performance optimization

        FP32 provides full precision (e.g., 3.14159265), while FP16 (3.14) and BF16 (3.1) reduce precision to improve speed and efficiency, commonly used on GPUs and during training. 
        Quantized formats like INT8 (127, -45), INT4 (7, -3), and INT2 (1, 0) compress models by limiting value ranges, with UINT8 (0–255) used for unsigned data in hardware accelerators. 
        Extreme compression includes Binary (0/1) and Ternary (-1, 0, 1), while Mixed Precision combines formats (e.g., weights in INT8 = 45, activations in FP16 = 3.14) for balanced performance.
                
        2. Pruning → Removes unnecessary weights or neurons
        3. Model Distillation → Transfers knowledge from a large model to a smaller one.



# Vector Database:-

1. In **Pinecone**, each record must have an ID and a vector and can also attach metadata for filtering. Metadata keys are strings, and values can be strings, numbers, booleans, or lists of strings.


**JSON:-**
{
  "id": "doc_101_chunk_03",
  "values": [0.021, -0.118, 0.442, 0.009, -0.331],
  "metadata": {
    "document_id": "doc_101",
    "chunk_id": 3,
    "title": "Azure Enterprise Agent Design",
    "source": "sharepoint",
    "department": "architecture",
    "created_at": "2026-03-20",
    "tags": ["azure", "mcp", "rac"],
    "is_active": true
  }
}

2. **FAISS** is not really a full database like Pinecone. It is a similarity search library for dense vectors, so usually keep:

vectors in a FAISS index, IDs in the index or an ID map, metadata/text in a separate store such as SQLite, Postgres, or a document store.

**FAISS index side:-**

faiss_index = {
  "dimension": 768,
  "index_type": "IndexIVFFlat",
  "metric": "cosine_or_l2",
  "vectors": [
    {"faiss_id": 1001, "embedding": [0.021, -0.118, 0.442, 0.009, -0.331]},
    {"faiss_id": 1002, "embedding": [0.155, -0.084, 0.391, 0.013, -0.210]}
  ]
}


**Factors:**

1. Non-deterministic Planning vs Deterministic Execution (outputs vary due to sampling (temperature, top-p, nucleus sampling)
2. Tool Invocation Failures (Schema + Parsing), repair prompts
3. State Persistence & Checkpointing (event sourcing)
4. Context Packing & Token Optimization
5. RAG Retrieval Failure Modes
6. Async Orchestration & Workflow Control (Async frameworks (asyncio, futures), DAG execution engines (LangGraph-style), Retry strategies:exponential backoff, circuit breakers, Task queues (Celery, Kafka))
7. Evaluation (Evals) Complexity
8. Latency Explosion (Cache embeddings)
9. Secure Code Execution (Sandboxing)
10. Observability & Debugging




