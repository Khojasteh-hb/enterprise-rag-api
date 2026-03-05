import os
import time
from dotenv import load_dotenv

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


# ---- Paths ----
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "sample.txt")
INDEX_PATH = os.path.join(BASE_DIR, "vectorstore", "faiss_index")


def create_index(file_path: str):

    load_dotenv()

    print("Loading document...")
    loader = TextLoader(file_path)
    documents = loader.load()

    print("Splitting into chunks...")
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150
    )

    chunks = splitter.split_documents(documents)

    print(f"Created {len(chunks)} chunks")

    print("Creating embeddings...")
    start_time = time.time()

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.from_documents(chunks, embeddings)

    end_time = time.time()
    print(f"Embedding time: {round(end_time - start_time, 2)} seconds")

    print("Saving FAISS index locally...")
    vectorstore.save_local(INDEX_PATH)

    print("Index created successfully!")


if __name__ == "__main__":
    create_index(DATA_PATH)
