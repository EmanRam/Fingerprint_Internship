# Task 2 — Document Loading & Chunking

**Course topic:** Document loaders and text splitters.
**Scaffolding:** 🟢 Guided — fill in the `# TODO`s in `starter.py`.
**Time budget:** ~half a day.

## Why this task
Retrieval quality is decided *before* you ever embed anything — at the chunking
stage. Chunks that are too big bury the answer in noise; chunks that are too
small lose context. This task builds intuition for that trade-off.

## Goal
1. Load every document in `data/` into LangChain `Document` objects.
2. Split them with a `RecursiveCharacterTextSplitter`.
3. **Experiment** with chunk size and overlap and observe the effect.

## Steps
1. Complete the TODOs in `starter.py`.
2. Run it with a few different `chunk_size` / `chunk_overlap` settings.
3. Answer the reflection questions at the bottom of `starter.py` in `NOTES.md`.

## Done when…
- [ ] You load all 4 markdown files and print how many `Document`s were loaded.
- [ ] You split them and print the chunk count for at least 3 different chunk sizes.
- [ ] Each chunk keeps its source filename in `metadata["source"]`.
- [ ] In `NOTES.md`, you explain what `chunk_overlap` is for and when large vs.
      small chunks are better.

## Stretch
- Add a **token-based** splitter (`RecursiveCharacterTextSplitter.from_tiktoken_encoder`)
  and compare chunk counts vs. the character-based one.
- Load a PDF (drop any PDF into `data/`) with `PyPDFLoader`.
