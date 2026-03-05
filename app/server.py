import os
from fastapi import FastAPI
from pydantic import BaseModel

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.chat_models import ChatOllama
from langchain_core.messages import HumanMessage


app = FastAPI(title="Enterprise RAG API")


class QuestionRequest(BaseModel):
    question: str


# ---- Paths ----
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX_PATH = os.path.join(BASE_DIR, "vectorstore", "faiss_index")


def load_vectorstore():
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.load_local(
        INDEX_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )

    return vectorstore


# load vectorstore once at startup
vectorstore = load_vectorstore()


# Ollama connection
ollama_base = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

llm = ChatOllama(
    model="mistral",
    base_url=ollama_base
)


@app.post("/ask")
def ask_question(request: QuestionRequest):

    docs = vectorstore.similarity_search(request.question, k=3)

    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
You are an industrial maintenance assistant.
Use the following context to answer the question clearly and concisely.

Context:
{context}

Question:
{request.question}

Answer:
"""

    response = llm.invoke([HumanMessage(content=prompt)])

    return {
        "question": request.question,
        "answer": response.content
    }


@app.get("/health")
def health():
    return {"status": "ok"}
