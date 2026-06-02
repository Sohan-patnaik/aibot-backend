# 🤖 Master AI — Custom Chatbot SaaS Backend

> A production-ready REST API that lets users **upload documents and spin up their own AI-powered chatbots** — all with a single endpoint call.

[![Live Demo](https://img.shields.io/badge/Live%20App-how--you--think.vercel.app-blue?style=for-the-badge)](https://how-you-think.vercel.app)
[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://docker.com)

---

## 🚀 What This Project Does

**Master AI** is the backend engine for a SaaS platform that enables any user to create a custom AI chatbot trained on their own documents (PDFs). Users upload a file, the system processes and indexes it, and a conversational agent becomes immediately queryable against that knowledge base.

Think of it as a self-service "ChatGPT for your documents" — built from scratch with a full RAG (Retrieval-Augmented Generation) pipeline.

---

## ✨ Key Features

- **Document Ingestion** — Upload PDFs via a REST endpoint; the system parses, chunks, and embeds them automatically
- **Hybrid Retrieval (RAG)** — Combines semantic vector search (FAISS) with BM25 keyword search for more accurate answers
- **Multi-LLM Support** — Integrates Google Gemini (`langchain-google-genai`) and NVIDIA AI endpoints for flexible model choice
- **Persistent Storage** — Bot knowledge bases are stored in Supabase (PostgreSQL + pgvector), enabling multi-user, multi-bot scenarios
- **Containerized** — Ships with a production Dockerfile; one command to deploy anywhere
- **Modular Architecture** — Clean separation of routes, controllers, and services for maintainability and scalability

---

## 🛠 Tech Stack

| Layer | Technology |
|---|---|
| **Framework** | FastAPI + Uvicorn |
| **AI / LLM** | LangChain, Google Gemini, NVIDIA AI Endpoints |
| **Retrieval** | FAISS (vector search) + BM25 (keyword search) |
| **Embeddings** | LangChain Google GenAI Embeddings |
| **Database** | Supabase (Postgres) |
| **Document Parsing** | PyPDF |
| **Containerization** | Docker |
| **Language** | Python 3.11 |

---

## 📁 Project Structure

```
saas-backend/
├── app.py                  # FastAPI app entry point — routes wired here
├── routes/
│   ├── upload.py           # POST /create-bot — document ingestion endpoint
│   └── agent.py            # POST /chat — conversational agent endpoint
├── controllers/            # Request validation & orchestration logic
├── services/               # Core business logic (RAG pipeline, LLM calls)
├── Dockerfile              # Production container config
└── requirements.txt        # Python dependencies
```

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api` | Health check — confirms service is running |
| `POST` | `/create-bot` | Upload a PDF to create a personalized bot |
| `POST` | `/chat` | Send a message and get an AI response from the bot |

---

## ⚙️ Getting Started

### Prerequisites
- Python 3.11+
- Docker (optional)
- Supabase account
- Google Gemini API key
- NVIDIA AI Endpoints API key

### Local Setup

```bash
# 1. Clone the repository
git clone https://github.com/Sohan-patnaik/saas-backend.git
cd saas-backend

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure environment variables
cp .env.example .env
# Fill in: GOOGLE_API_KEY, NVIDIA_API_KEY, SUPABASE_URL, SUPABASE_KEY

# 4. Start the server
uvicorn app:app --reload
```

API will be available at `http://localhost:8000`  
Interactive docs at `http://localhost:8000/docs`

### Docker Setup

```bash
docker build -t master-ai .
docker run -p 8000:8000 --env-file .env master-ai
```

---

## 🧠 How the RAG Pipeline Works

```
User uploads PDF
      │
      ▼
 PDF Parsed (PyPDF)
      │
      ▼
 Text Chunked (LangChain TextSplitter)
      │
      ▼
 Embeddings Generated (Google GenAI)
      │
      ▼
 Stored in FAISS + Supabase
      │
      ▼
 User sends chat message
      │
      ▼
 Hybrid Retrieval (FAISS + BM25)
      │
      ▼
 Context + Query sent to LLM
      │
      ▼
 Accurate, grounded answer returned
```

---

## 🔑 Environment Variables

| Variable | Description |
|---|---|
| `GOOGLE_API_KEY` | Google Gemini API key |
| `NVIDIA_API_KEY` | NVIDIA AI Endpoints key |
| `SUPABASE_URL` | Your Supabase project URL |
| `SUPABASE_KEY` | Your Supabase anon/service key |

---

## 💡 Engineering Highlights

- **Hybrid retrieval** using both FAISS semantic search and BM25 keyword ranking improves answer relevance over pure vector search alone
- **Multi-LLM architecture** (Gemini + NVIDIA) means the system isn't locked to a single provider — easy to swap or A/B test models
- **Supabase as the persistence layer** enables a true multi-tenant setup where each user's bot data is isolated and queryable
- **FastAPI** with async support allows concurrent bot conversations without blocking, important for a SaaS workload

---

## 🌐 Live Deployment

The frontend consuming this API is deployed at: **[how-you-think.vercel.app](https://how-you-think.vercel.app)**

---

## 📄 License

This project is open source. Feel free to explore, fork, and build on it.

---

*Built by [Sohan Patnaik](https://github.com/Sohan-patnaik)*
