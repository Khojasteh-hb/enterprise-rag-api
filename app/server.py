from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from pydantic import BaseModel

from app.rag import ask_question as rag_ask


app = FastAPI(title="Enterprise RAG API")


class QuestionRequest(BaseModel):
    question: str


@app.post("/ask")
def ask(request: QuestionRequest):
    answer = rag_ask(request.question)

    return {
        "question": request.question,
        "answer": answer
    }


@app.get("/health")
def health():
    return {"status": "ok"}
