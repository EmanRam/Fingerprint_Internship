"""
Task 3 — FastAPI service skeleton.

The plumbing is wired: app object, lifespan startup, Pydantic models, route
declarations, SSE streaming. Your logic goes in the TODO spots.

Copy this to `app/main.py`, then:

    make run
    # or: uvicorn app.main:app --reload

Docs at http://localhost:8000/docs
"""

from __future__ import annotations

import os
import uuid
from contextlib import asynccontextmanager
from typing import Any

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from sse_starlette.sse import EventSourceResponse

# ---------------------------------------------------------------------------
# Startup / shutdown
# ---------------------------------------------------------------------------

# Process-wide handles, populated once at startup. NOT per request — building the
# graph loads (or worse, builds) the FAISS index, and doing that per request is
# the single most expensive mistake available to you here.
STATE: dict[str, Any] = {"graph": None}


@asynccontextmanager
async def lifespan(app: FastAPI):
    # TODO 1: compile the graph ONCE here.
    #   from <your capstone graph module> import build_graph
    #   STATE["graph"] = build_graph()
    #
    # Log a line saying whether the index was loaded from disk or built from
    # scratch — Task 1 asked for exactly this and Task 5 will consume it.
    yield
    # Shutdown: flush anything that needs flushing.


app = FastAPI(
    title="Northwind Internal Docs Assistant",
    version="1.0.0",
    lifespan=lifespan,
)


# ---------------------------------------------------------------------------
# Request / response models — nothing untyped crosses this boundary
# ---------------------------------------------------------------------------

class ChatRequest(BaseModel):
    question: str = Field(min_length=1, max_length=2000)
    session_id: str = Field(default_factory=lambda: str(uuid.uuid4()))


class ChatResponse(BaseModel):
    answer: str
    sources: list[str]
    node_path: list[str]
    session_id: str
    trace_id: str | None = None


class FeedbackRequest(BaseModel):
    trace_id: str
    rating: int = Field(ge=-1, le=1, description="-1 down, 0 neutral, 1 up")
    comment: str | None = None


class ErrorResponse(BaseModel):
    """One error shape for the whole API. A client never sees a stack trace."""
    error: str
    detail: str | None = None
    request_id: str | None = None


# ---------------------------------------------------------------------------
# Session store
# ---------------------------------------------------------------------------

# TODO 2: implement per-session history.
#
# A module-level dict works for one worker and silently breaks for two — each
# process gets its own copy, so a user hitting worker B loses the conversation
# they started on worker A. You do NOT have to solve that today, but you DO have
# to know it and answer for it in the PR.
#
# Whatever you choose, it needs: get(session_id), append(session_id, messages),
# clear(session_id), and some TTL so memory doesn't grow forever.

_SESSIONS: dict[str, list] = {}


def get_history(session_id: str) -> list:
    raise NotImplementedError("TODO 2")


def append_turn(session_id: str, question: str, answer: str) -> None:
    raise NotImplementedError("TODO 2")


# ---------------------------------------------------------------------------
# Core call — one place the graph is invoked from
# ---------------------------------------------------------------------------

def run_graph(question: str, session_id: str) -> dict:
    """Invoke the compiled graph and normalise its output.

    TODO 3: build the input state (question, history, and the rest of the fields
            your GraphState declares), invoke STATE["graph"], and return a dict
            with: answer, sources, node_path.

    Two things to get right:
      * `sources` is the deduplicated set of source filenames from the SURVIVING
        documents — the ones that passed grading, not everything retrieved.
      * `node_path` needs graph.stream(..., stream_mode="updates"), the same
        technique you used in Task 8 to print each question's node path. Reuse it.
    """
    raise NotImplementedError("TODO 3")


# ---------------------------------------------------------------------------
# Endpoints
# ---------------------------------------------------------------------------

@app.post("/chat", response_model=ChatResponse)
async def chat(req: ChatRequest) -> ChatResponse:
    """TODO 4: call run_graph, persist the turn to session history, return it."""
    raise NotImplementedError("TODO 4")


@app.post("/chat/stream")
async def chat_stream(req: ChatRequest):
    """Stream tokens as they're generated, then a final event with the metadata.

    TODO 5: yield SSE events.

    Suggested protocol — the UI and your tests both depend on it, so write it
    down in the README:
        {"event": "token", "data": "..."}      one per token
        {"event": "done",  "data": {...}}      sources + node_path + trace_id
        {"event": "error", "data": {...}}      structured, same shape as ErrorResponse

    Note the honest constraint: your graph does routing and grading BEFORE it
    generates, so nothing streams for the first few seconds. Decide what the
    user sees during that window — a status event per node is a good answer, and
    it makes the agentic behaviour visible instead of feeling like a hang.
    """

    async def event_generator():
        raise NotImplementedError("TODO 5")
        yield  # unreachable; keeps this a generator

    return EventSourceResponse(event_generator())


@app.get("/healthz")
async def healthz() -> dict:
    """Liveness: is the process up? Cheap, and it MUST NOT call the model.

    A health check that hits the LLM will page you at 3am because your provider
    had a slow minute, and will cost money on every probe.
    """
    return {"status": "ok"}


@app.get("/readyz")
async def readyz() -> dict:
    """Readiness: can this instance actually serve traffic?

    TODO 6: report whether the graph is compiled and the index is loaded.
            Return 503 if not — that's the signal a load balancer acts on.
    """
    raise NotImplementedError("TODO 6")


@app.post("/feedback")
async def feedback(req: FeedbackRequest) -> dict:
    """TODO 7: send the rating to LangSmith.

    Look at langsmith.Client().create_feedback(run_id=..., key="user_rating",
    score=...). This is what makes the 👍/👎 buttons in the UI worth having.
    """
    raise NotImplementedError("TODO 7")


@app.delete("/session/{session_id}")
async def reset_session(session_id: str) -> dict:
    """TODO 8: clear this session's history. Idempotent — clearing a session
    that doesn't exist is a 200, not a 404."""
    raise NotImplementedError("TODO 8")


# ---------------------------------------------------------------------------
# Error handling — one shape, everywhere
# ---------------------------------------------------------------------------

@app.exception_handler(Exception)
async def unhandled_exception_handler(request: Request, exc: Exception):
    """TODO 9: log the full exception server-side (with the request id), and
    return an ErrorResponse to the client. Never leak the traceback.

    Task 8 will build timeouts and retries on top of this. Get the shape right now.
    """
    raise NotImplementedError("TODO 9")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app,
        host=os.getenv("API_HOST", "0.0.0.0"),
        port=int(os.getenv("API_PORT", "8000")),
    )
