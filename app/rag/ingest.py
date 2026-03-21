# filename: app/rag/ingest.py

from pathlib import Path

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings


PROJECT_ROOT = Path(__file__).resolve().parents[2]
RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw" / "ai_notes.txt"
VECTOR_STORE_PATH = PROJECT_ROOT / "data" / "vector_store"


def load_raw_text() -> str:
    if not RAW_DATA_PATH.exists():
        raise FileNotFoundError(f"知识库文件不存在: {RAW_DATA_PATH}")

    return RAW_DATA_PATH.read_text(encoding="utf-8")


def split_text(text: str) -> list[str]:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=150, # 每个文本块的最大字符数
        chunk_overlap=30, # 相邻文本块之间的重叠字符数
        separators=["\n\n", "\n", "。", " ", ""],
    )
    chunks = splitter.split_text(text)

    clean_chunks = [chunk.strip() for chunk in chunks if chunk.strip()]
    if not clean_chunks:
        raise ValueError("文本切分后没有有效内容，请检查知识库文件。")

    return clean_chunks


def build_vector_store():
    text = load_raw_text()
    chunks = split_text(text)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vector_store = FAISS.from_texts(chunks, embedding=embeddings)
    VECTOR_STORE_PATH.mkdir(parents=True, exist_ok=True)
    vector_store.save_local(str(VECTOR_STORE_PATH))

    print(f"知识库切分完成，共 {len(chunks)} 个文本块。")
    print(f"FAISS 索引已保存到: {VECTOR_STORE_PATH}")


if __name__ == "__main__":
    build_vector_store()