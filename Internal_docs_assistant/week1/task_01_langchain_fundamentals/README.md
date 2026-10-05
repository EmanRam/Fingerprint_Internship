# Task 1 — LangChain Fundamentals (LCEL)

**Course topic:** LangChain basics — chat models, prompt templates, output
parsers, and the LangChain Expression Language (LCEL) `|` pipe.
**Scaffolding:** 🟢 Guided — fill in the `# TODO`s in `starter.py`.
**Time budget:** ~half a day.

## Why this task
Before you can do RAG, you need to be fluent in the three primitives every
LangChain program is built from: a **prompt**, a **model**, and an **output
parser**, chained together with LCEL. RAG is just this chain with a retrieval
step bolted on the front — so nail this first.

## Goal
Build three small chains:
1. A **one-shot chain**: prompt → model → string output.
2. A **structured chain**: force the model to return validated JSON (use a Pydantic
   schema + `with_structured_output`).
3. A **"summarize this doc" chain** that takes a document from `data/` as input.

## Steps
1. Open `starter.py`. Run it first to confirm your keys work.
2. Complete each `# TODO`. Read the comments — they explain the concept.
3. Experiment: change the temperature, swap the provider in `.env`, tweak prompts.

## Done when…
- [ ] `python starter.py` runs top to bottom with no errors.
- [ ] Chain 1 prints a plain-string answer.
- [ ] Chain 2 returns a Python object matching the Pydantic schema (not raw text).
- [ ] Chain 3 produces a 3-bullet summary of `data/product_specs.md`.
- [ ] You can explain, in `NOTES.md`, what the `|` operator actually does.

## Stretch
- Add a `RunnableParallel` that runs the summary and a sentiment classification at
  the same time and merges the results into one dict.
