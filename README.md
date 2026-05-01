# documind-ai
AI-powered PDF Q&amp;A system using FastAPI, embeddings, and local LLMs

# 📄 DocuMind

AI-powered document Q&A system that allows users to upload PDFs and ask questions.

## 🚀 Features
- Upload PDF documents
- Semantic search using embeddings
- AI-powered answers using local LLM (Ollama)
- FastAPI backend + simple frontend

## 🛠 Tech Stack
- Python, FastAPI
- Sentence Transformers
- FAISS (vector search)
- Ollama (LLM)
- HTML/CSS/JS frontend

## ⚙️ Setup

```bash
git clone https://github.com/YOUR_USERNAME/documind-ai.git
cd documind-ai/backend
pip install -r requirements.txt
uvicorn app.main:app --reload
