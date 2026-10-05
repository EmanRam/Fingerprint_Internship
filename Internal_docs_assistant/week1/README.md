# RAG Engineering Internship — Week 1 Task Series

Welcome! This repository is your workbench for **Week 1** of the AI Engineering
internship. It runs alongside the Udemy course
**"Ultimate RAG Bootcamp Using LangChain, LangGraph & LangSmith."**

You will build a Retrieval-Augmented Generation (RAG) system from the ground up:
starting with a single LLM call, and finishing with an **agentic, evaluated,
production-shaped assistant** that answers questions over a company's internal
documents.

---

## How this works

The week is a ladder of **8 small tasks** followed by a **capstone project**.
Each rung reuses what you built on the last one, so *don't* delete your work as
you go — later tasks import from earlier ones.

| # | Task | Course topic it reinforces | Scaffolding |
|---|------|----------------------------|-------------|
| 1 | LangChain fundamentals (LCEL, prompts, output parsers) | LangChain basics | 🟢 Guided (starter + TODOs) |
| 2 | Document loading & chunking | Loaders, text splitters | 🟢 Guided |
| 3 | Embeddings & vector stores | Embeddings, FAISS/Chroma | 🟢 Guided |
| 4 | Naive RAG pipeline | Retrievers, RAG chain | 🟢 Guided |
| 5 | Conversational RAG with memory | History-aware retrieval | 🟡 Mixed |
| 6 | Advanced retrieval (multi-query, MMR, re-rank, hybrid) | Retrieval quality | 🟡 Mixed |
| 7 | LangSmith tracing & evaluation | LangSmith | 🟡 Mixed |
| 8 | Agentic RAG with LangGraph (routing + self-correction) | LangGraph | 🔴 Spec-only |
| ⭐ | **Capstone:** Internal Docs Assistant | Everything | 🔴 Spec-only |

🟢 = skeleton code with `# TODO` markers to fill in.
🟡 = partial skeleton + a written spec; you design more of it.
🔴 = a requirements spec and acceptance criteria; you build it from scratch.

---

## Setup (do this first)

1. **Python 3.10+** is required. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate        # Windows: .venv\Scripts\activate
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Add your API keys.** Copy the example env file and fill it in:
   ```bash
   cp .env.example .env
   ```
   You need at minimum a model provider key. The starter code defaults to
   **OpenAI** but is written to also work with **Groq**, **Ollama** (local, free),
   or **HuggingFace** — see `common/utils.py`. For Task 7 onward you also need a
   **LangSmith** key (free tier at https://smith.langchain.com).

4. **Verify your setup:**
   ```bash
   python common/utils.py
   ```
   You should see a one-line reply from the model. If you do, you're ready.

> **Never commit your `.env` file or API keys.** It is already in `.gitignore`.

---

## Working rules

- **One branch per task** (e.g. `git checkout -b task-01`), open a small PR to
  your mentor when done. This mirrors real engineering workflow and gives you
  review practice.
- Every task folder has its own `README.md` with the goal, steps, and a
  **"Done when…"** checklist. Read it fully before you start.
- Prefer understanding over copying. If you paste code from the course, add a
  comment in your own words explaining *why* it works.
- Log your questions and blockers in `NOTES.md` (create one) — mentors review it.

## Sample data

The `data/` folder contains a small fictional company's internal docs
(HR policies, IT FAQ, an employee handbook, and product specs). All tasks and
the capstone use this corpus so you can focus on the RAG mechanics, not on
finding data. You are welcome to add more documents.

Good luck — build something you're proud to demo on Friday. 🚀
