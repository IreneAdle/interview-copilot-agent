# filename: tests/test_tools.py

from app.tools.calculator_tool import calculator_tool
from app.rag.retriever import retrieve_documents


def test_calculator():
    expr = "(25.5 * 3 + 18) / 2"
    result = calculator_tool.invoke({"expression": expr})
    assert result == "47.25", f"calculator result error: {result}"
    print("calculator test passed")


def test_rag():
    docs = retrieve_documents("什么是 Agent？", top_k=2)
    assert len(docs) > 0, "rag returned no documents"
    print("rag test passed")


if __name__ == "__main__":
    test_calculator()
    test_rag()
    print("all tests passed")