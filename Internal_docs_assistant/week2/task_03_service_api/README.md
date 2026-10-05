# Task 3 — Wrap It In A Service

**Focus:** FastAPI, token streaming, sessions that outlive a browser tab.
**Scaffolding:** 🔴 Spec-only — an `app/` skeleton is provided so you don't burn
time on plumbing, but every endpoint body is yours.
**Time budget:** one full day (Tuesday).
**Branch:** `week2/task-03-api`

---

## Why this task

Streamlit is a demo surface. A **service** is what other software talks to, and
the constraints are different: concurrent callers, streaming responses, sessions
that survive a page refresh, errors that must be structured rather than printed
to a terminal nobody is watching.

This is the largest single step of the week and the one that most changes how you
think about the system. After it, there is exactly **one** place the RAG logic
lives, and everything else — the UI, the eval harness, the cost report — is a
client of it.

---

## What to build

### The endpoints

| Method | Path | Behaviour |
|---|---|---|
| `POST` | `/chat` | `{question, session_id}` → answer, sources, and the node path the graph took. Non-streaming. |
| `POST` | `/chat/stream` | Same input. Streams tokens via SSE, then a final event carrying sources and node path. |
| `GET` | `/healthz` | Liveness. Cheap. **Must not call the model.** |
| `GET` | `/readyz` | Readiness — is the index loaded and the graph compiled? |
| `POST` | `/feedback` | `{trace_id, rating, comment}` → logged to LangSmith. |
| `DELETE` | `/session/{session_id}` | Clears that session's memory. |

### The requirements

- **Pydantic models** for every request and response. No bare dicts crossing the
  boundary.
- **Session memory** that survives across requests and stays isolated per
  `session_id`. Think about — and write down — what happens with two workers.
- **Structured JSON errors.** A client should never receive a stack trace. Define
  an error shape and use it everywhere.
- **The index and graph load once at startup**, not per request. Use FastAPI's
  lifespan handler.
- **The Streamlit UI calls the API over HTTP** and imports no graph code. When
  you're done, `grep -r "build_graph" app/ui.py` should find nothing.

---

## What's provided

`app_skeleton.py` — the FastAPI plumbing: app object, lifespan hook, Pydantic
models, route declarations, and the SSE wiring, all with `# TODO` markers where
your logic plugs in. Copy it to `app/main.py` to begin.

---

## Done when…

- [ ] All six endpoints respond correctly, and `/docs` renders the OpenAPI page.
- [ ] `curl -N` against `/chat/stream` shows tokens arriving **incrementally**, not
      in one lump. Commit the terminal transcript or a short recording.
- [ ] Two different `session_id`s hold independent conversations — proved by a
      test, not a claim. Name the test in `week2/RESULTS.md`.
- [ ] The Streamlit UI works entirely through HTTP.
- [ ] `week2/RESULTS.md` records p50 and p95 latency over 20 requests, for both
      `/chat` and `/chat/stream` (time-to-first-token **and** time-to-last-token).
- [ ] Killing and restarting the service does not re-embed the corpus.
- [ ] `/healthz` responds in under 50 ms and makes no model call.

---

## Two questions to answer in the PR

1. **Where does session state live, and what breaks if you run two workers?**
   You don't have to solve it. You have to know it's there and say what you'd do.
2. **What does `/readyz` check that `/healthz` doesn't, and why does the
   difference matter to a load balancer?**

---

## Stretch

- **Concurrency:** fire 5 simultaneous requests. Does latency degrade? If so, find
  where — the LLM provider's rate limit, a lock in your session store, or the
  embedding call — and write down which. Record it in `RESULTS.md`.
- Return the `trace_id` in every response so `/feedback` can reference it without
  the client guessing.
- Add `X-Request-ID` passthrough now; Task 5 will thank you.
