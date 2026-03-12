
# Enterprise RAG API

![Python](https://img.shields.io/badge/Python-3.10-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-API-green)
![FAISS](https://img.shields.io/badge/Vector%20DB-FAISS-orange)
![LangChain](https://img.shields.io/badge/LangChain-framework-yellow)
![LLM](https://img.shields.io/badge/LLM-Mistral-purple)
![RAG](https://img.shields.io/badge/Architecture-RAG-red)
![Docker](https://img.shields.io/badge/Docker-ready-blue)


A modular **Retrieval-Augmented Generation (RAG)** system built with FastAPI, FAISS vector search, and LLM providers (OpenAI or Ollama).

This project demonstrates how to build a complete RAG pipeline including:

- document ingestion
- semantic vector indexing
- retrieval
- LLM-based answer generation
- evaluation of system responses

---

## Architecture

```
                +-------------------+
                |    User Query     |
                +---------+---------+
                          |
                          v
                +-------------------+
                |    FastAPI API    |
                +---------+---------+
                          |
                          v
                +-------------------+
                |   FAISS Retrieval |
                |   (Vector Search) |
                +---------+---------+
                          |
                          v
                +-------------------+
                |  Relevant Context |
                +---------+---------+
                          |
                          v
                +-------------------+
                |    LLM Provider   |
                |                   |
                |  OpenAI / Ollama |
                +---------+---------+
                          |
                          v
                +-------------------+
                |  Generated Answer |
                +-------------------+
                
``` 

---

## Features

   - Retrieval-Augmented Generation (RAG)

   - FAISS vector search

   - HuggingFace sentence-transformer embeddings

   - OpenAI support

   - Ollama local model support

   - LLM provider abstraction layer

   - FastAPI REST API

   - Docker & Docker Compose support

   - Evaluation script for testing the RAG pipeline

---

## Project Structure

```text
enterprise-rag
│
├── app
│   ├── server.py
│   ├── ask.py
│   ├── build_index.py
│   ├── cli.py
│   └── llm
│       └── provider.py
│
├── data
│   └── sample.txt
│
├── vectorstore
│   └── faiss_index
│
├── tests
│   └── evaluate_rag.py
│
├── images
│   └── evaluation.png
│
├── Dockerfile
├── docker-compose.yml
├── start.sh
├── requirements.txt
└── README.md

```

---

## Setup

### Clone the repository:

```bash
git clone <repo-url>
cd enterprise-rag
```

### Create environment variables:

```bash
cp .env.example .env
```
Edit `.env` and add your OpenAI key if needed.

### Running locally
Activate the virtual environment:

```bash
source venv/bin/activate
```

### Install dependencies:

```bash
pip install -r requirements.txt
```

---

#### Start Ollama

Make sure Ollama is running before starting the API.

```bash
ollama run mistral
```

--- 

### Build the FAISS index:

```bash
python app/build_index.py
```

### Start the API:

```bash
uvicorn app.server:app --reload
```

The API will be available at:

```bash 
http://localhost:8000
```
---

## Example API Request

```bash
curl -X POST http://localhost:8000/ask \
-H "Content-Type: application/json" \
-d '{"question":"What is preventive maintenance?"}'
```

Example response:

```json
{
  "question": "...",
  "answer": "..."
}
```

---

## Running with Docker

Build and start the container:

```bash 
docker compose up --build
```

The API will be available at:

```bash
http://localhost:8000
```
---

## Evaluation

A simple evaluation script is included to test the RAG pipeline.

Run:

```bash
python tests/evaluate_rag.py
```

### The script sends sample questions to the API and reports:

   - generated answers

   - response latency

### Hardware used for evaluation:

   - CPU-only inference

   - LLM: Mistral (Ollama) or OpenAI models

   - Embedding: sentence-transformers/all-MiniLM-L6-v2

   - Vector store: FAISS

Example output:
![API Evaluation](images/evaluation.png)

---

## LLM Providers

The system supports multiple LLM providers.

Configured via environment variables.

### OpenAI

```bash
LLM_PROVIDER=openai
OPENAI_API_KEY=your_key
```

### Ollama

```bash
LLM_PROVIDER=ollama
OLLAMA_BASE_URL=http://host.docker.internal:11434
```

---

## Environment Variables

Example `.env` configuration:

```env
LLM_PROVIDER=openai
OPENAI_API_KEY=your_api_key

# optional for Ollama
OLLAMA_BASE_URL=http://host.docker.internal:11434
```

---

## Future Improvements

   - Cloud deployment

   - Hybrid search (BM25 + vector search)

   - Streaming responses

   - RAG evaluation metrics

   - Better prompt engineering

---

## License

MIT License

---

