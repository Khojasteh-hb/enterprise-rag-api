#!/bin/bash

echo "Building FAISS index..."
python build_index.py

echo "Starting FastAPI server..."
uvicorn server:app --host 0.0.0.0 --port 8000
