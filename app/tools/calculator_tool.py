#filename: app/tools/caculator_tool.py

import ast
import operator
from langchain.tools import tool


_ALLOWED_OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
}


def _safe_eval(node):
    if isinstance(node, ast.Expression):
        return _safe_eval(node.body)

    if isinstance(node, ast.Constant):
        if isinstance(node.value, (int, float)):
            return node.value
        raise ValueError("只支持整数或浮点数。")

    if isinstance(node, ast.Num):  # 兼容旧版本 Python
        return node.n

    if isinstance(node, ast.BinOp):
        left = _safe_eval(node.left)
        right = _safe_eval(node.right)
        op_type = type(node.op)

        if op_type not in _ALLOWED_OPERATORS:
            raise ValueError(f"不支持的运算符: {op_type.__name__}")

        return _ALLOWED_OPERATORS[op_type](left, right)

    if isinstance(node, ast.UnaryOp):
        operand = _safe_eval(node.operand)
        op_type = type(node.op)

        if op_type not in _ALLOWED_OPERATORS:
            raise ValueError(f"不支持的单目运算符: {op_type.__name__}")

        return _ALLOWED_OPERATORS[op_type](operand)

    raise ValueError(f"不支持的表达式类型: {type(node).__name__}")


@tool
def calculator_tool(expression: str) -> str:
    """
    用于执行基础数学表达式计算。
    支持 +、-、*、/、括号和小数。
    输入应为纯数学表达式字符串，例如: '(25.5 * 3 + 18) / 2'
    """
    try:
        parsed = ast.parse(expression, mode="eval")
        result = _safe_eval(parsed)
        return str(result)
    except Exception as e:
        return f"计算失败: {str(e)}"