#!/bin/bash

set -e

if [ ! -d "vectorstore/faiss_index" ]; then
  echo "FAISS index not found. Building index..."
  python app/build_index.py
else
  echo "FAISS index already exists."
fi

echo "Starting FastAPI server..."

exec uvicorn app.server:app --host 0.0.0.0 --port 8000
