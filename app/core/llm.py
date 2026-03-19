# filename: app/core/llm.py


from langchain_openai import ChatOpenAI

from app.core.config import get_settings


def get_llm() -> ChatOpenAI:
    settings = get_settings()

    # 初始化 ChatOpenAI 实例
    llm = ChatOpenAI(
        model=settings.model_name,
        api_key=settings.dashscope_api_key,
        base_url=settings.dashscope_base_url,
        temperature=0,
    )
    return llm