# filename: app/agent/agent_executor.py

from langchain.agents import create_agent

from app.core.llm import get_llm
from app.memory.memory_manager import memory
from app.prompts.system_prompt import SYSTEM_PROMPT
from app.tools.calculator_tool import calculator_tool
from app.tools.rag_tool import rag_search_tool


def build_agent():
    llm = get_llm()
    tools = [calculator_tool, rag_search_tool]

    agent = create_agent(
        model=llm,
        tools=tools,
        system_prompt=SYSTEM_PROMPT,
    )
    return agent


def _extract_text_from_response(response: dict) -> str:
    messages = response.get("messages", [])
    if not messages:
        return "未获得有效响应。"

    last_message = messages[-1]
    content = getattr(last_message, "content", None)

    if isinstance(content, str):
        return content

    if isinstance(content, list):
        text_parts = []
        for item in content:
            if isinstance(item, dict) and item.get("type") == "text":
                text_parts.append(item.get("text", ""))
        return "\n".join(text_parts).strip() or str(content)

    return str(content)


def run_agent(user_input: str, thread_id: str = "default") -> str:
    agent = build_agent()

    history = memory.get_messages(thread_id)
    current_messages = history + [{"role": "user", "content": user_input}]

    response = agent.invoke({"messages": current_messages})
    final_text = _extract_text_from_response(response)

    memory.add_user_message(thread_id, user_input)
    memory.add_assistant_message(thread_id, final_text)

    return final_text


def clear_memory(thread_id: str = "default") -> None:
    memory.clear(thread_id)