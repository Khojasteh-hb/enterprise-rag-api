import os

from langchain_community.chat_models import ChatOllama
from langchain_openai import ChatOpenAI


def get_llm():

    provider = os.getenv("LLM_PROVIDER", "openai")

    if provider == "ollama":
        return ChatOllama(
            model="mistral",
            base_url=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
        )

    elif provider == "openai":
        return ChatOpenAI(
            model="gpt-4o-mini",
            api_key=os.getenv("OPENAI_API_KEY")
        )

    else:
        raise ValueError(f"Unsupported LLM provider: {provider}")
