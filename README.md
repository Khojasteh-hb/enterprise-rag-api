# Enterprise RAG System with Local LLM


![Python](https://img.shields.io/badge/Python-3.10-blue)
![FastAPI](https://img.shields.io/badge/API-FastAPI-009688)
![LangChain](https://img.shields.io/badge/LLM-LangChain-orange)
![VectorDB](https://img.shields.io/badge/Vector%20Database-FAISS-red)
![Model](https://img.shields.io/badge/Model-Mistral-purple)
![Deployment](https://img.shields.io/badge/Deployment-Docker-blue)


## 1. Overview

This project implements a Retrieval-Augmented Generation (RAG) system using a local Large Language Model. The system retrieves relevant information from a document corpus using
 vector similarity search and generates answers based on the retrieved context.

The pipeline combines document ingestion, text chunking, embedding generation, FAISS vector indexing, and a local Mistral model served via Ollama. A FastAPI service exposes
 the system through a REST API that allows users to query the knowledge base using natural language.

The project demonstrates how enterprise documentation or operational manuals can be transformed into an interactive AI-powered knowledge assistant.

---

## 2. Architecture

```text
   User Query
      │
      ▼
   FastAPI REST API
      │
      ▼
   Query Processing
      │
      ▼
   Vector Similarity Search (FAISS)
      │
      ▼
   Retrieve Top-K Relevant Chunks
      │
      ▼
   Prompt Construction
      │
      ▼
   Local LLM (Mistral via Ollama)
      │
      ▼
   Generated Answer
      │
      ▼
   JSON Response

```

---

