## 🌐 语言

- 中文
- [English](README.md)

# Interview Copilot Agent（面试辅助智能体）

一个基于 LangChain 构建的多工具 AI Agent 项目。
该项目展示了如何将大语言模型（LLM）与外部工具（RAG 检索、计算工具）结合，并支持简单多轮对话能力。

---

## 🚀 项目功能

* 🔧 **LangChain Agent**：自动根据问题选择工具
* 📚 **RAG 检索工具**：基于 FAISS + 向量检索的本地知识库
* 🧮 **计算工具**：支持数学表达式精确计算
* 🧠 **短期记忆（Memory）**：支持多轮对话上下文
* ⚙️ **模块化设计**：结构清晰，易于扩展

---

## 🧠 系统架构

```text
用户输入
   ↓
LangChain Agent
   ↓
 ┌───────────────┬────────────────┐
 ↓               ↓                ↓
RAG 工具     计算工具        LLM 直接回答
 ↓
FAISS 向量数据库
```

---

## 📂 项目结构

```text
app/
  agent/       # Agent 组装与执行
  core/        # 配置管理与 LLM 初始化
  tools/       # 工具定义（Calculator / RAG）
  rag/         # 知识库构建与检索
  memory/      # 简单会话记忆
  prompts/     # 系统提示词
  main.py      # 命令行入口

data/
  raw/             # 原始知识库
  vector_store/    # FAISS 索引

tests/             # 基础测试脚本
```

---

## ⚙️ 环境准备

### 1. 克隆项目

```bash
# HTTPS (recommended)
git clone https://github.com/IreneAdle/interview-copilot-agent.git

# SSH (if configured)
git clone git@github.com:IreneAdle/interview-copilot-agent.git

cd interview-copilot-agent
```

---

### 2. 创建虚拟环境

```bash
python -m venv .venv
```

> Linux / macOS:

```bash
source .venv/bin/activate
```

> Windows (PowerShell):

```powershell
.venv\Scripts\Activate.ps1
```

> Windows (cmd):

```cmd
.venv\Scripts\activate.bat  
```

---

### 3. 安装依赖

```bash
pip install -r requirements.txt
```

---

### 4. 配置环境变量

在项目根目录创建 `.env` 文件：

```env
DASHSCOPE_API_KEY=你的API_KEY
DASHSCOPE_BASE_URL=模型服务地址
MODEL_NAME=模型名称
```

示例（阿里百炼 Qwen）：

DASHSCOPE_API_KEY=sk-xxxx

DASHSCOPE_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1

MODEL_NAME=qwen3.5-flash

---

## 📚 构建知识库（RAG）

```bash
python -m app.rag.ingest
```

该步骤会完成：

* 文本切分
* 向量化（embedding）
* 构建 FAISS 索引

---

## ▶️ 启动 Agent

```bash
python -m app.main
```

---

## 🧪 运行测试

```bash
python tests/test_tools.py
```

---

## 💬 示例问答

```text
用户：什么是 Agent？

Agent：Agent（智能体）是能够感知环境、进行决策并执行行动以达成目标的系统。它通常由大模型、工具调用、记忆机制和任务规划组成，使 AI 从“对话”进化为“执行任务”。
```

```text
用户：(25.5 * 3 + 18) / 2 等于多少？

Agent：47.25
```

```text
用户：我刚才问了什么？

Agent：您刚才询问的是一个数学计算问题：“(25.5 * 3 + 18) / 2 等于多少？”
```

```text
用户：还有什么？

Agent：在此之前，您还询问了“什么是 Agent”，这是一个关于 AI 概念的问题。
```

```text
用户：先解释什么是 RAG，再计算 18 / 3 + 2

Agent：
RAG（检索增强生成）是一种结合信息检索与大语言模型的技术，通过先检索外部知识再生成回答，从而提升准确性并减少幻觉。

计算结果：18 / 3 + 2 = 8
```

```text
用户：clear

系统：当前会话记忆已清空。
```

```text
用户：我刚才问了什么？

Agent：这是当前会话中的第一条问题，暂无历史记录。
```


---

## ✨ 设计亮点

* **工具驱动架构**：将能力封装为 Tool，由 Agent 自动调度
* **RAG 增强生成**：通过外部知识库提升回答准确性
* **计算与语言能力解耦**：避免大模型直接心算带来的误差
* **简单会话记忆机制**：支持多轮上下文理解
* **配置与代码解耦**：通过 `.env` 管理模型与 API Key

---

## 🔮 后续可扩展方向

* 增加 Web Search / API Tool
* 引入持久化 Memory（数据库 / Redis）
* 优化检索策略（混合检索 / rerank）
* 构建 Web UI（Streamlit / FastAPI）
* 多 Agent 协作系统

---

## 📝 License

MIT License
