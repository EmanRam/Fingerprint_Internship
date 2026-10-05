# Task 4 — API image skeleton.
# Copy to the repo root as `Dockerfile` and fill in the TODOs.

# ---------------------------------------------------------------------------
# Stage 1 — build
# Compile wheels here so the runtime stage stays clean and small.
# ---------------------------------------------------------------------------
FROM python:3.12-slim AS builder

WORKDIR /build

# TODO 1: install build dependencies if any of your packages need compiling,
#         then clean up apt lists in the SAME RUN layer (otherwise the cleanup
#         doesn't shrink anything — layers are immutable).

# Dependencies FIRST, source code LAST. Docker caches layers in order, so a code
# edit should not reinstall faiss.
# Two files with the same name, so give each its own name (copying both to ./
# would make the second silently overwrite the first).
COPY week1/requirements.txt ./requirements-week1.txt
COPY week2/requirements.txt ./requirements-week2.txt
# TODO 2: build wheels into /build/wheels
#         pip wheel --no-cache-dir --wheel-dir /build/wheels #             -r requirements-week1.txt -r requirements-week2.txt


# ---------------------------------------------------------------------------
# Stage 2 — runtime
# ---------------------------------------------------------------------------
FROM python:3.12-slim

# TODO 3: create a non-root user and switch to it before running the app.
#         Running as root in a container is the default and it is not fine.
#         Remember the app needs write access to the index volume.

WORKDIR /app

# TODO 4: copy the wheels from the builder stage and install them, then delete
#         the wheels in the same layer.

# TODO 5: copy only what the service needs — app/, common/, and your graph and
#         ingestion modules.
#         NOT the whole repo. Use .dockerignore to enforce it.

# Where the persisted FAISS index lives. docker-compose mounts a named volume
# here so the index survives image rebuilds.
ENV INDEX_PATH=/data/faiss_index
# TODO 6: create /data and make it writable by the non-root user.

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    API_HOST=0.0.0.0 \
    API_PORT=8000

EXPOSE 8000

# TODO 7 (stretch): add a HEALTHCHECK against /healthz.

# TODO 8: the run command. Use exec form so signals reach the process and
#         `docker stop` doesn't take 10 seconds to time out.
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]


# ---------------------------------------------------------------------------
# Before you open the PR, verify — don't assume:
#   docker build -t northwind-api .
#   docker history northwind-api        # <- no API key in ANY layer
#   docker images northwind-api         # <- record the size in RESULTS.md
#   docker run --rm northwind-api whoami   # <- must not say root
# ---------------------------------------------------------------------------
