# filename: app/tools/rag_tool.py

from langchain.tools import tool

from app.rag.retriever import retrieve_documents


@tool
def rag_search_tool(query: str) -> str:
    """
    用于检索本地知识库中的相关内容。
    适合回答 AI 基础概念、LangChain、Agent、RAG、Transformer、Prompt Engineering 等知识性问题。
    输入应为用户的问题或检索查询。
    """
    try:
        docs = retrieve_documents(query, top_k=3)
        if not docs:
            return "未检索到相关知识。"

        formatted = []
        for i, doc in enumerate(docs, start=1):
            formatted.append(f"[检索片段 {i}]\n{doc}")

        return "\n\n".join(formatted)
    except Exception as e:
        return f"RAG 检索失败: {str(e)}"