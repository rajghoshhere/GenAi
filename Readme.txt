# 🧠🖼️🛠️ AI Toolkit Playground

Welcome to the **AI Toolkit Playground** — a hands-on repository featuring multiple GenAI-based capabilities built using LangChain, Stable Diffusion, and multi-agent orchestration. This repo includes:

- 🔍 A Retrieval-Augmented Generation (RAG) system from local documents  
- 🎨 A prompt-based image generator using Stable Diffusion  
- 🤖 A ReAct-based multi-tool agent that informs, entertains, and searches

---

## 📁 Project Structure

### 1. 📚 RAG-Based Q&A System

This module uses a **Retrieval-Augmented Generation** pipeline to answer questions based on your **local documents** (PDF, text, etc.).

- **Process**:
  - Documents are chunked using LangChain text splitters
  - Embedded and stored in a vector store (like FAISS or Chroma)
  - At query time, relevant chunks are retrieved
  - Answer is generated using a powerful LLM (like OpenAI or Databricks LLM)

- **Use Case**: Ask questions like “What is covered in chapter 3?” from your own files.

---

### 2. 🖼️ Image Generator with Stable Diffusion

This is a **text-to-image pipeline** using the **Stable Diffusion** model.

- **Features**:
  - Accepts natural language prompts from the user
  - Generates realistic or artistic images
  - Runs locally or via a HuggingFace endpoint

- **Example Prompt**:  
  _"A futuristic cityscape at sunset with flying cars"_

---

### 3. 🤹 Multi-Agent ReAct Tool: Search, Watch, Laugh

A fun and functional **multi-tool agent** built with LangChain's ReAct framework.

- **What it does**:
  1. Takes a user query (e.g., a topic)
  2. Searches the web using DuckDuckGo
  3. Finds a relevant YouTube video
  4. Ends with a lighthearted joke about the topic

- **Technologies Used**:
  - `Tavily` or `DuckDuckGoSearchRun` for web search
  - Wikipedia wrapper for quick facts
  - Joke generator using LLM (e.g., Databricks or OpenAI)
  - LangChain `Tool`, `AgentExecutor`, and ReAct agent

- **Use Case**: Learn something new and end with a smile.

---

## 🛠️ Requirements

- Python 3.8+
- `langchain`, `openai`, `faiss-cpu` or `chromadb`
- `stable-diffusion`, `diffusers`, `transformers`
- (Optional) `Tavily`, `DuckDuckGo`, or `YouTube Data API`

Install everything via:

```bash
pip install -r requirements.txt
