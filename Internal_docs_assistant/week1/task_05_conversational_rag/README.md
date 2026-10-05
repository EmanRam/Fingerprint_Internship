# Task 5 — Conversational RAG with Memory

**Course topic:** History-aware retrieval, chat memory, session state.
**Scaffolding:** 🟡 Mixed — light skeleton in `starter.py`, but you design the
history-aware retriever yourself.
**Time budget:** ~one day.

## Why this task
Real users ask follow-ups: *"How much PTO do I get?"* → *"And can I carry it
over?"* A naive retriever embeds "can I carry it over?" with no idea what "it" is,
and retrieves garbage. A **history-aware retriever** first rewrites the follow-up
into a standalone question using the chat history, *then* retrieves.

## Goal
Extend your Task 4 RAG into a multi-turn chatbot that:
1. Rewrites follow-up questions into standalone questions using history.
2. Retrieves on the rewritten question.
3. Answers with the retrieved context **and** the conversation so far.
4. Keeps per-session history so two users don't share memory.

## Recommended building blocks
- `create_history_aware_retriever`
- `create_stuff_documents_chain`
- `create_retrieval_chain`
- `RunnableWithMessageHistory` + an in-memory `ChatMessageHistory` store keyed by
  `session_id`

(You may instead build the equivalent by hand in LCEL — either is fine, but you
must be able to explain how the question gets contextualized.)

## Done when…
- [ ] This exact sequence works in one session:
      `"How much PTO do I get?"` → `"Can I carry it over to next year?"` and the
      second answer correctly talks about the 5-day carry-over cap **without you
      repeating the word "PTO."**
- [ ] A different `session_id` does **not** see the first session's history.
- [ ] The bot still refuses to answer things outside the docs.

## Stretch
- Add a `/reset` command that clears a session's memory.
- Trim history to the last N turns to control token cost, and note the trade-off.
