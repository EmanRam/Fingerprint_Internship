# Task 4 — Containerize & Configure

**Focus:** making it run somewhere that isn't your laptop.
**Scaffolding:** 🟡 Mixed — Dockerfile and compose skeletons provided.
**Time budget:** half a day (Wednesday AM).
**Branch:** `week2/task-04-docker`

---

## Why this task

"It works on my machine" is the classic failure here: a hardcoded Windows path
that only resolves from one directory on one OS, or a script that only runs from
the repo root. A container is the forcing function: it either runs
somewhere else or it doesn't, and there's no arguing with it.

There's a second lesson here. A provider URL or model name hardcoded into
`common/utils.py` (say, an OpenRouter `base_url` in the OpenAI branch) silently
breaks for anyone holding a different key. **Configuration is not code.**

---

## What to build

### The image

- A `Dockerfile` for the API. Slim base image, dependencies in their own layer so
  code changes don't reinstall the world, and a **non-root user**.
- Multi-stage if you can manage it — build wheels in one stage, copy into a clean
  runtime stage.

### The composition

- `docker-compose.yml` bringing up API and UI together with one command.
- The FAISS index mounted as a **named volume**. Without this, every image rebuild
  discards the index and silently re-embeds — the most common Week 1 cost mistake, in a new place.

### The configuration

Everything below moves to environment variables with sensible defaults. Nothing
in this list may remain a literal in the source:

| Setting | Currently |
|---|---|
| Model / provider | env ✓ |
| `base_url` | Wherever your provider code sets it (often hardcoded) |
| Retriever `k` | hardcoded `4` in several places |
| Chunk size / overlap | hardcoded `600` / `80` |
| Index path | derived from `__file__` |
| API host / port | — |

Use `pydantic-settings` for a typed `Settings` object rather than scattered
`os.getenv` calls. One import, one source of truth, and it validates at startup
instead of failing on the first request.

---

## What's provided

- `Dockerfile` — a skeleton with the stages marked and `# TODO`s.
- `docker-compose.yml` — services declared, wiring left to you.

---

## Done when…

- [ ] `docker compose up` from a **clean checkout** gives a working assistant, with
      only `.env` supplied. Test this by cloning into a fresh directory — not by
      trusting it.
- [ ] `docker history <image>` shows **no API key** in any layer. Check it, don't
      assume it.
- [ ] Switching provider (OpenAI ↔ Groq ↔ OpenRouter) requires editing `.env` only.
      Demonstrate the switch.
- [ ] Image size recorded in `week2/RESULTS.md`, with one sentence on the biggest
      contributor to it.
- [ ] The container runs as a non-root user (`docker exec ... whoami` proves it).
- [ ] Restarting the containers does not re-embed — the volume holds.

---

## Traps

- **The `.env` file must not be `COPY`'d into the image.** Add it to
  `.dockerignore` and pass it at runtime. A key baked into a layer survives
  deletion and is visible to anyone who pulls the image.
- **`faiss-cpu` and the ML stack are large.** Don't be surprised by a multi-GB
  image; be able to say *why* it's that size and what you'd cut.
- **Don't `COPY . .` before `pip install`.** Every code edit then reinstalls every
  dependency, and your build loop goes from seconds to minutes.

---

## Stretch

- Add a `HEALTHCHECK` to the Dockerfile pointing at `/healthz`.
- Get the image under 1 GB and record what you dropped to do it.
