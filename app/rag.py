# app/rag.py

import os
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.messages import HumanMessage
from app.llm.provider import get_llm

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX_PATH = os.path.join(BASE_DIR, "vectorstore", "faiss_index")


def load_vectorstore():
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    return FAISS.load_local(
        INDEX_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )


vectorstore = load_vectorstore()
llm = get_llm()


def ask_question(question: str, k: int = 3):
    docs = vectorstore.similarity_search(question, k=k)

    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
You are an industrial maintenance assistant.
Use the following context to answer clearly.

Context:
{context}

Question:
{question}

Answer:
"""

    response = llm.invoke([HumanMessage(content=prompt)])

    return response.content
