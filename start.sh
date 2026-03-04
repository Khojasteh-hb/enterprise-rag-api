#!/bin/bash

if [ ! -d "faiss_index" ]; then
  echo "Building FAISS index..."
  python rag_index.py
fi

uvicorn server:app --host 0.0.0.0 --port 8000
