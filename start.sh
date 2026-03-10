#!/bin/bash

echo "Building FAISS index..."
python app/build_index.py

echo "Starting FastAPI server..."
uvicorn app.server:app --host 0.0.0.0 --port 8000
