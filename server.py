from fastapi import FastAPI
from pydantic import BaseModel
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

app = FastAPI(title="Enterprise RAG API")


class QuestionRequest(BaseModel):
    question: str


def load_vectorstore():
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.load_local(
        "faiss_index",
        embeddings,
        allow_dangerous_deserialization=True
    )

    return vectorstore


vectorstore = load_vectorstore()


@app.post("/ask")
def ask_question(request: QuestionRequest):
    docs = vectorstore.similarity_search(request.question, k=3)

    results = [
        {
            "content": doc.page_content
        }
        for doc in docs
    ]

    return {
        "question": request.question,
        "results": results
    }
