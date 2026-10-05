"""
Fast tier — no network, no API key. Must run in under 5 seconds.

These tests assert on STRUCTURE and WIRING, never on model wording. A test that
says `assert answer == "You get 20 days"` fails next Tuesday for no reason and
you will learn to ignore it. Assert on what must be true.

Run with:  make check
"""

import pytest


# ===========================================================================
# THE REGRESSION TEST
#
# This is the most important test you will write this week. A classic capstone
# bug: the app imports build_graph from the Task 8 module instead of the
# capstone's own graph. The app still runs and still answers, but it has no
# history node, so multi-turn memory is silently dead, and the Task 8 retriever
# rebuilds the index instead of loading the persisted one.
#
# Write this so that pointing the app at the wrong graph turns it RED.
# ===========================================================================

def test_app_graph_has_contextualize_node():
    """The graph the app imports must support conversation history.

    TODO 1: import build_graph exactly the way app.py imports it — not the way
            you know is correct. The point is to test what the app really does.

            Then assert your history-aware node (e.g. "contextualize") is in
            the compiled graph's nodes.
            Look at: graph.get_graph().nodes
    """
    raise NotImplementedError


def test_app_graph_state_accepts_history():
    """TODO 2: assert the state schema has a `history` field.

    Without it, the history the app passes in is silently dropped. Check the
    graph's state schema annotations, or invoke with a history key and assert
    it isn't rejected.
    """
    raise NotImplementedError


# ===========================================================================
# GRAPH WIRING
# ===========================================================================

def test_graph_compiles():
    """TODO 3: build_graph() returns without raising."""
    raise NotImplementedError


def test_every_conditional_edge_target_exists():
    """A conditional edge mapping to a node name that doesn't exist is a
    runtime error waiting for the right question to trigger it.

    TODO 4: walk graph.get_graph().edges and assert every target is either a
            real node name or END.
    """
    raise NotImplementedError


def test_all_nodes_reachable_from_start():
    """TODO 5: walk the edges from START and assert every declared node is
    reachable. An unreachable node is dead code you'll debug for an hour.
    """
    raise NotImplementedError


# ===========================================================================
# PROMPT AND FORMATTING CONTRACTS
# ===========================================================================

def test_format_docs_tags_every_source(sample_docs):
    """Citations are a required capability; they start here.

    TODO 6: call format_docs(sample_docs) and assert each document's source
            filename appears in the output.
    """
    raise NotImplementedError


def test_generate_prompt_contains_refusal_instruction():
    """The anti-hallucination rule is non-negotiable — so pin it with a test.

    TODO 7: assert the exact string "I don't know based on the provided
            documents." appears in the generate node's system prompt.

    This is also the test Task 7's CI gate will rely on: if someone weakens the
    prompt, this goes red before the eval even runs.
    """
    raise NotImplementedError


def test_generate_refuses_when_no_documents_survive(fake_llm):
    """When grade_documents filters everything out, generate must emit the
    refusal without calling the model at all.

    TODO 8: call generate({"documents": [], ...}) and assert the refusal string
            is returned AND that fake_llm.calls is empty — no model call, no cost.
    """
    raise NotImplementedError


# ===========================================================================
# INDEX PERSISTENCE  (the other half of the wrong-graph bug)
# ===========================================================================

def test_vectorstore_loads_from_disk_when_index_exists(temp_index_dir, monkeypatch):
    """TODO 9: with the index directory present, assert build_or_load_vectorstore
            calls load_local and NOT from_documents. Re-embedding on every start
            is the thing this whole test is guarding.
    """
    raise NotImplementedError


def test_vectorstore_builds_when_index_missing(temp_index_dir, monkeypatch):
    """TODO 10: the inverse — with no index directory, it must build and save."""
    raise NotImplementedError


# ===========================================================================
# TERMINATION  (stretch)
# ===========================================================================

@pytest.mark.skip(reason="stretch goal — remove the skip when you attempt it")
def test_graph_terminates_at_max_retries(fake_llm):
    """Force the worst path: every doc graded irrelevant, every generation
    graded ungrounded. The graph must still reach END.

    TODO 11: drive it with a FakeLLM configured to always fail the graders,
             and assert the run completes without hitting the recursion limit.
    """
    raise NotImplementedError
