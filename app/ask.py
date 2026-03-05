import os
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.documents import Document


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


def query_index(question: str):
    vectorstore = load_vectorstore()

    docs = vectorstore.similarity_search(question, k=3)

    print("\nTop relevant chunks:\n")

    for i, doc in enumerate(docs, 1):
        print(f"Result {i}:")
        print(doc.page_content)
        print("-" * 50)


if __name__ == "__main__":
    print("RAG CLI ready. Type your question (or 'exit' to quit):\n")

    while True:
        question = input(">> ")

        if question.lower() == "exit":
            break

        query_index(question)
