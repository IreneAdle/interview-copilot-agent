## 🌐 Language

- English
- [中文](README_zh.md)

# Interview Copilot Agent

A lightweight multi-tool AI Agent built with LangChain.
This project demonstrates how to combine LLMs with external tools such as RAG retrieval and calculators, along with simple conversational memory.

---

## 🚀 Features

* 🔧 **LangChain Agent** for automatic tool selection
* 📚 **RAG Tool** using FAISS + local embeddings
* 🧮 **Calculator Tool** for precise numerical computation
* 🧠 **Short-term Memory** for multi-turn conversations
* ⚙️ **Modular design** for easy extension

---

## 🧠 Architecture

```text
User Input
   ↓
LangChain Agent
   ↓
 ┌───────────────┬────────────────┐
 ↓               ↓                ↓
RAG Tool     Calculator Tool     LLM Direct Answer
 ↓
FAISS Vector Store
```

---

## 📂 Project Structure

```text
app/
  agent/       # Agent orchestration
  core/        # Config & LLM initialization
  tools/       # Tool definitions
  rag/         # Knowledge ingestion & retrieval
  memory/      # Simple conversation memory
  prompts/     # System prompt
  main.py      # CLI entry point

data/
  raw/             # Raw knowledge base
  vector_store/    # FAISS index

tests/             # Basic test scripts
```

---

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/IreneAdle/interview-copilot-agent.git
cd interview-copilot-agent
```

---

### 2. Create virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

> Windows (PowerShell):

```powershell
.venv\Scripts\Activate.ps1
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure environment variables

Create a `.env` file in the root directory:

```env
DASHSCOPE_API_KEY=your_api_key
DASHSCOPE_BASE_URL=your_model_url
MODEL_NAME=your_model_name
```

Example (Qwen via DashScope):

DASHSCOPE_API_KEY=sk-xxxx
DASHSCOPE_BASE_URL=https://dashscope.aliyuncs.com/compatible-mode/v1
MODEL_NAME=qwen3.5-flash

---

## 📚 Build Knowledge Base

```bash
python -m app.rag.ingest
```

This step:

* Splits documents
* Generates embeddings
* Builds FAISS index

---

## ▶️ Run the Agent

```bash
python -m app.main
```

---

## 🧪 Run Tests

```bash
python tests/test_tools.py
```

---

## 💬 Example Usage

```text
What is an Agent?
(25.5 * 3 + 18) / 2
Explain RAG, then calculate 18 / 3 + 2
```

---

## 🧩 Design Highlights

* Separation of concerns: LLM / Tools / RAG / Memory
* Tool abstraction for extensibility
* Retrieval-augmented generation for factual grounding
* Lightweight in-memory session management
* Config-driven model switching

---

## 🔮 Future Improvements

* Add web search tool
* Support persistent memory (database)
* Improve retrieval quality (reranking / hybrid search)
* Build web UI (Streamlit / FastAPI)
* Multi-agent collaboration

---

## 📝 License

MIT License
