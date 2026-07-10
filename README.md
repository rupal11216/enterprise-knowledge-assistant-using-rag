# enterprise-knowledge-assistant-using-rag

An AI-powered enterprise knowledge assistant that leverages Retrieval-Augmented Generation (RAG) to deliver accurate, context-aware responses from multiple knowledge sources. The application combines Large Language Models (LLMs), semantic search, vector databases, and structured document retrieval to provide grounded answers while minimizing hallucinations.

---

# Overview

Enterprise knowledge is often scattered across FAQs, technical documentation, and historical support records, making information retrieval slow and inefficient. This project demonstrates how a Retrieval-Augmented Generation (RAG) system can consolidate multiple knowledge sources, retrieve the most relevant information semantically, and generate reliable responses grounded in enterprise data.

The assistant retrieves information from structured FAQs, resolved support tickets, and technical documentation using independent semantic retrieval pipelines before combining the retrieved context for response generation. It provides both a Streamlit-based conversational interface and a command-line interface while gracefully handling unsupported or out-of-scope queries.

---

# Key Features

- Retrieval-Augmented Generation (RAG) pipeline
- Multi-source semantic retrieval across FAQs, support tickets, and technical documentation
- Independent retrieval from multiple ChromaDB collections
- Sentence Transformer embeddings for semantic search
- Context-aware response generation using Groq-hosted Qwen3-32B
- Interactive Streamlit web application
- Command-line interface for local interaction
- Modular document ingestion pipeline
- Recursive chunking for long-form documents
- Graceful handling of unsupported and out-of-scope queries
- Lightweight and extensible architecture

---

# Tech Stack

## Languages & Frameworks

- Python
- Streamlit
- LangChain

## AI Technologies

- Retrieval-Augmented Generation (RAG)
- Generative AI
- Semantic Search
- Sentence Transformers
- Large Language Models (LLMs)

## LLM

- Groq
- Qwen3-32B

## Vector Database

- ChromaDB

## Knowledge Sources

- CSV
- SQLite
- PDF Documents

---

# System Architecture

```
                        User
                          │
                          ▼
             Streamlit / CLI Interface
                          │
                          ▼
                 RAG Orchestrator
                          │
            ┌─────────────┼─────────────┐
            ▼             ▼             ▼
         FAQ Store   Support Tickets   PDF Guide
            │             │             │
            └─────────────┼─────────────┘
                          ▼
                  ChromaDB Collections
                          │
                          ▼
       Sentence Transformer Embeddings
                          │
                          ▼
                 Groq (Qwen3-32B)
                          │
                          ▼
                Context-Aware Response
```

---

# Example Queries

- Why is my mobile internet so slow?
- My calls keep dropping. What should I do?
- How do I activate international roaming?
- Why is my bill higher than usual this month?
- My phone shows "SIM not detected" after restarting.
- How do I enable Wi-Fi calling?
- I was charged for roaming despite having a roaming bundle.
- How do I unlock my phone for another network?

---

# Project Highlights

- Built a Retrieval-Augmented Generation (RAG) application capable of retrieving information from multiple enterprise knowledge sources before generating responses.
- Implemented independent semantic retrieval pipelines for FAQs, resolved support tickets, and technical documentation using dedicated ChromaDB vector collections.
- Combined semantic retrieval with LLM reasoning to generate accurate, context-aware responses grounded in enterprise knowledge.
- Developed a modular ingestion pipeline supporting CSV, SQLite, and PDF knowledge sources.
- Designed the assistant to recognize unsupported or out-of-domain queries and respond appropriately instead of generating unsupported information.
- Built both web-based and command-line interfaces using a shared retrieval pipeline.

---

# Design Decisions

- Maintained separate vector collections for FAQs, support tickets, and technical documentation to preserve source-specific retrieval quality.
- Applied recursive chunking only to long-form PDF documents while keeping structured knowledge sources unchunked.
- Performed semantic retrieval independently across each knowledge source before merging retrieved context.
- Used deterministic LLM settings for consistent and reproducible responses.
- Designed a modular architecture to simplify the addition of future enterprise knowledge sources.

---

# Running the Project

1. Clone the repository.

2. Create a local Python environment using your preferred environment manager.

3. Install the required project dependencies.

4. Create a local `.env` file and add the required API credentials.

5. Build the vector database by running:

```bash
python ingest_faq.py
python ingest_pdf.py
python ingest_tickets.py
```

6. Launch the Streamlit application:

```bash
streamlit run app.py
```

Or run the command-line interface:

```bash
python main.py
```

---

# Repository Notes

- Local environment variables (`.env`) have been intentionally excluded from the repository to protect API credentials.
- The project was developed using **uv** for dependency and environment management. Environment-specific files (such as `uv.lock`) and local virtual environment artifacts have intentionally been omitted to keep the repository lightweight and focused on the application source code.
- Before running the application, create a local `.env` file and add the required API credentials.

---

# Limitations

- Response quality depends on the completeness and quality of the indexed knowledge base.
- The application does not maintain conversational memory across sessions.
- Retrieval is based solely on semantic similarity without reranking.
- Optimized for enterprise knowledge retrieval rather than open-domain conversations.

---

# Future Enhancements

- Hybrid semantic and keyword retrieval
- Retrieval reranking
- Source attribution in generated responses
- Conversation memory
- Incremental document indexing
- Multi-language support
- Role-based knowledge access
- User feedback-driven retrieval optimization

---

# License

This project is licensed under the MIT License.
