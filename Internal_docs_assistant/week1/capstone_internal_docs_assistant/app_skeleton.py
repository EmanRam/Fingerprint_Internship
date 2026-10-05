"""
Capstone — Streamlit app skeleton.

The UI plumbing is done for you. Plug your RAG backend into the two TODO spots,
then copy this file to app.py and run:

    streamlit run capstone_internal_docs_assistant/app.py

You are expected to back this with your LangGraph agentic RAG (Task 8), your
retriever (Task 6), and session memory (Task 5).
"""

import sys
import uuid
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

import streamlit as st

from common.utils import get_llm  # noqa: F401  (you'll import your own graph too)


# ---------------------------------------------------------------------------
# TODO A: Build (and cache) your RAG backend.
#   Return something with an .invoke() that takes a question + session_id and
#   returns an answer plus its source documents. Reuse your Task 8 graph.
#   Use @st.cache_resource so the index/graph is built ONCE, not per message.
# ---------------------------------------------------------------------------
@st.cache_resource
def get_backend():
    # e.g. from task_08_langgraph_agentic_rag.graph import build_graph
    #      return build_graph()
    raise NotImplementedError("Plug in your agentic RAG graph here (TODO A).")


def answer_question(backend, question: str, session_id: str) -> dict:
    """
    TODO B: Call your backend and return a dict like:
        {"answer": "...", "sources": ["hr_policies.md", ...]}
    Wire session_id through so multi-turn memory is per-session.
    """
    raise NotImplementedError("Call your backend and shape the response (TODO B).")


# ---------------------------------------------------------------------------
# UI — provided. You shouldn't need to change much below this line.
# ---------------------------------------------------------------------------
st.set_page_config(page_title="Northwind Internal Assistant", page_icon="🤖")
st.title("🤖 Northwind Internal Docs Assistant")
st.caption("Ask about HR policies, IT procedures, and product specs.")

if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())
if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:
    st.write(f"Session: `{st.session_state.session_id[:8]}`")
    if st.button("🔄 Reset conversation"):
        st.session_state.messages = []
        st.session_state.session_id = str(uuid.uuid4())
        st.rerun()

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Ask a question about company policies…"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking…"):
            backend = get_backend()
            result = answer_question(backend, prompt, st.session_state.session_id)
            answer = result.get("answer", "")
            sources = result.get("sources", [])
            st.markdown(answer)
            if sources:
                st.caption("📎 Sources: " + ", ".join(sources))
    st.session_state.messages.append({"role": "assistant", "content": answer})
