# Task 2 — The Golden-Path Test Harness

**Focus:** regression safety. Making integration bugs impossible to repeat.
**Scaffolding:** 🟡 Mixed — pytest layout and fixtures given, the tests are yours.
**Time budget:** half a day (Monday PM).
**Branch:** `week2/task-02-tests`

---

## Why this task

Week 1 tested components one at a time; the **joints between them** were never
tested. A capstone can have a perfect graph and still run the wrong one, because
the app imports it from the wrong module. That is exactly the class of bug
automated tests exist to catch, and it is why
this task comes before any new feature: from here on, everything you build has
something that fails loudly when you break it.

The single most valuable test you will write this week is the one that goes red
if the app is ever wired to the wrong graph.

---

## What to build

A `tests/` package with two tiers.

### Fast tests — no API calls, must run in under 5 seconds

These are the ones that run on every PR, so they can't cost money or take time.
Mock the LLM (there's a `fake_llm` fixture in `conftest.py`) and assert on
**structure and wiring**, not on model output:

- The graph compiles.
- The graph the **app imports** contains your history-aware node (e.g. `contextualize`). ← the regression test
- Every node named in a conditional-edge mapping actually exists in the graph.
- `format_docs` emits a `[source]` tag for every document it's given.
- The generate prompt contains the exact refusal string.
- `build_or_load_vectorstore` loads from disk when the index directory exists,
  and only builds when it doesn't.

### Live tests — real API calls, marked `@pytest.mark.live`

One per capstone must-have. These cost money, so they run on demand:

- A grounded question returns the right fact **and** a citation.
- An out-of-scope question returns the refusal, not a guess.
- A two-turn follow-up resolves correctly.
- Two different `session_id`s do not see each other's history.

### One command

`make check` runs lint + fast tests. `make check-live` runs the live tier. Both
are already stubbed in `week2/Makefile` — make them real.

---

## What's provided

- `tests/conftest.py` — fixtures for a fake LLM, a temp index directory, and
  sample documents.
- `tests/test_graph_structure.py` — the fast tier, with `# TODO` markers.
- `tests/test_golden_path.py` — the live tier, with `# TODO` markers.

Copy these into a `tests/` directory at the repo root (not inside this task
folder — tests belong with the project).

---

## Done when…

- [ ] `make check` runs green in **under 5 seconds** with no API key set in the
      environment. Time it and record the number in `week2/RESULTS.md`.
- [ ] **The regression test works.** Point the app's import at a graph without the
      history node (e.g. your Task 8 graph), run `make check`, and show it
      **failing**. Then restore the correct import and show it passing. Put the
      failing output in your PR description.
- [ ] The live golden-path tests pass — at minimum the four must-haves (grounded
      answer with citation, refusal, two-turn follow-up, session isolation). The
      other stubs in `test_golden_path.py` are encouraged. Record total wall-clock
      time and API cost in `week2/RESULTS.md`.
- [ ] `week2/RESULTS.md` names which test file and function is the regression guard.
- [ ] The repo README documents both commands.

---

## A trap to avoid

Do not assert on the model's wording. `assert "20 days" in answer` is reasonable;
`assert answer == "You get 20 days of PTO per year."` is a test that will fail next
Tuesday for no reason, and you will learn to ignore it. Assert on the **facts and
structure** that must be true: the number appears, a source is cited, the refusal
string is present, the route taken was `retrieve`.

---

## Stretch

- Add a test that asserts the graph **terminates** for a question that forces the
  maximum retry path — that is, that `MAX_RETRIES` really bounds it.
- Add `pytest --durations=5` output to `RESULTS.md` so you know which test is
  slowest before it becomes a problem.
