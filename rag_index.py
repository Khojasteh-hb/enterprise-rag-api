import os
import time
from dotenv import load_dotenv

from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS


def create_index(file_path: str):
    load_dotenv()

    if not os.getenv("OPENAI_API_KEY"):
        raise ValueError("OPENAI_API_KEY not found in environment variables.")

    print("📄 Loading document...")
    loader = TextLoader(file_path)
    documents = loader.load()

    print("✂️ Splitting into chunks...")
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150
    )
    chunks = splitter.split_documents(documents)

    print(f"✅ Created {len(chunks)} chunks")

    print("🧠 Creating embeddings...")
    start_time = time.time()

    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(chunks, embeddings)

    end_time = time.time()
    print(f"⏱ Embedding time: {round(end_time - start_time, 2)} seconds")

    print("💾 Saving FAISS index locally...")
    vectorstore.save_local("faiss_index")

    print("🎉 Index created successfully!")


if __name__ == "__main__":
    create_index("sample.txt")
