"""
Shared helpers used across every task and the capstone.

The point of this module is to hide provider differences behind two functions:

    get_llm()         -> a LangChain chat model
    get_embeddings()  -> a LangChain embeddings object

so the rest of your code never hard-codes OpenAI/Groq/Ollama. Which provider is
used is controlled by LLM_PROVIDER / EMBEDDING_PROVIDER in your .env file.

You normally do NOT need to edit this file. Read it, though — understanding this
indirection is part of writing clean RAG code.
"""

from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv

# Load .env from the repo root regardless of where the script is launched from.
_REPO_ROOT = Path(__file__).resolve().parents[1]
load_dotenv(_REPO_ROOT / ".env")

DATA_DIR = _REPO_ROOT / "data"


def get_llm(temperature: float = 0.0, **kwargs):
    """Return a chat model based on the LLM_PROVIDER env var (default: openai)."""
    provider = os.getenv("LLM_PROVIDER", "openai").lower()

    if provider == "openai":
        from langchain_openai import ChatOpenAI
        return ChatOpenAI(model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
                          temperature=temperature, **kwargs)
    if provider == "groq":
        from langchain_groq import ChatGroq
        return ChatGroq(model=os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile"),
                        temperature=temperature, **kwargs)
    if provider == "ollama":
        from langchain_ollama import ChatOllama
        return ChatOllama(model=os.getenv("OLLAMA_MODEL", "llama3.1"),
                          temperature=temperature, **kwargs)
    if provider == "huggingface":
        from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
        endpoint = HuggingFaceEndpoint(
            repo_id=os.getenv("HF_MODEL", "HuggingFaceH4/zephyr-7b-beta"),
            temperature=max(temperature, 0.01),
        )
        return ChatHuggingFace(llm=endpoint)

    raise ValueError(f"Unknown LLM_PROVIDER: {provider!r}")


def get_embeddings(**kwargs):
    """Return an embeddings object based on EMBEDDING_PROVIDER (default: openai)."""
    provider = os.getenv("EMBEDDING_PROVIDER", "openai").lower()

    if provider == "openai":
        from langchain_openai import OpenAIEmbeddings
        return OpenAIEmbeddings(
            model=os.getenv("OPENAI_EMBED_MODEL", "text-embedding-3-small"), **kwargs)
    if provider in ("huggingface", "ollama", "groq"):
        # Groq has no embeddings API — fall back to a free local HF model.
        from langchain_huggingface import HuggingFaceEmbeddings
        return HuggingFaceEmbeddings(
            model_name=os.getenv("HF_EMBED_MODEL", "sentence-transformers/all-MiniLM-L6-v2"),
            **kwargs)

    raise ValueError(f"Unknown EMBEDDING_PROVIDER: {provider!r}")


if __name__ == "__main__":
    # Quick smoke test: `python common/utils.py`
    print(f"LLM provider     : {os.getenv('LLM_PROVIDER', 'openai')}")
    print(f"Embedding provider: {os.getenv('EMBEDDING_PROVIDER', 'openai')}")
    llm = get_llm()
    reply = llm.invoke("In one sentence, what is Retrieval-Augmented Generation?")
    print("\nModel says:", reply.content)
