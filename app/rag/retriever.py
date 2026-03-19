# filename: app/rag/retriever.py

from pathlib import Path
from typing import Optional

from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings


PROJECT_ROOT = Path(__file__).resolve().parents[2]
VECTOR_STORE_PATH = PROJECT_ROOT / "data" / "vector_store"

_embeddings: Optional[HuggingFaceEmbeddings] = None
_vector_store: Optional[FAISS] = None


def get_embeddings() -> HuggingFaceEmbeddings:
    global _embeddings

    if _embeddings is None:
        _embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
    return _embeddings


def load_vector_store() -> FAISS:
    global _vector_store

    if _vector_store is None:
        if not VECTOR_STORE_PATH.exists():
            raise FileNotFoundError(
                f"向量库不存在: {VECTOR_STORE_PATH}，请先运行 ingest.py 构建索引。"
            )

        embeddings = get_embeddings()
        _vector_store = FAISS.load_local(
            str(VECTOR_STORE_PATH),
            embeddings,
            allow_dangerous_deserialization=True,
        )

    return _vector_store


def retrieve_documents(query: str, top_k: int = 3) -> list[str]:
    vector_store = load_vector_store()
    docs = vector_store.similarity_search(query, k=top_k)
    return [doc.page_content for doc in docs]