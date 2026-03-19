# filename: app/main.py


from app.core.llm import get_llm
from app.tools.calculator_tool import calculator_tool
from app.rag.retriever import retrieve_documents
from app.agent.agent_executor import clear_memory, run_agent

# 测试大模型调用
# def main():
#     llm = get_llm()
#     print("LLM 初始化成功：", llm)

# 测试计算器工具调用
# def main():
#     expressions = [
#         "(25.5 * 3 + 18) / 2",
#         "1 + 2 * 3",
#         "-5 + 2.5",
#         "10 / 4",
#     ]

#     for expr in expressions:
#         result = calculator_tool.invoke({"expression": expr})
#         print(f"表达式: {expr}")
#         print(f"结果: {result}")
#         print("-" * 30)

# 测试检索器
# def main():
#     query = "什么是 Agent？"
#     docs = retrieve_documents(query, top_k=3)

#     print("查询问题：", query)
#     print("=" * 50)
#     for i, doc in enumerate(docs, start=1):
#         print(f"[结果 {i}]")
#         print(doc)
#         print("-" * 50)

# agent 测试
def main():
    thread_id = "default"
    print("Interview Copilot Agent 已启动。输入 quit 退出，输入 clear 清空记忆。")

    while True:
        user_input = input("\n你：").strip()

        if user_input.lower() in {"quit", "exit", "q"}:
            print("已退出。")
            break

        if user_input.lower() == "clear":
            clear_memory(thread_id)
            print("当前会话记忆已清空。")
            continue

        if not user_input:
            continue

        try:
            result = run_agent(user_input, thread_id=thread_id)
            print(f"\nAgent：{result}")
        except Exception as e:
            print(f"\n程序运行出错: {str(e)}")


if __name__ == "__main__":
    main()