"""
Live tier — real API calls. Costs money. Run on demand, not on every PR.

One test per capstone must-have. These are the four things a mentor will try in
the Friday demo, so they should be the four things a machine tries first.

Run with:  make check-live
"""

import pytest

pytestmark = pytest.mark.live


# ===========================================================================
# Must-have 1 & 4 — grounded answer, with a citation
# ===========================================================================

def test_grounded_answer_with_citation():
    """TODO 1: ask "How many sick days do I get per year?" through the same
            entry point the app uses.

    Assert:
      - the correct number appears in the answer
      - at least one source filename is returned
      - the source is one that could actually contain the fact

    Assert on the FACT, not the sentence. The wording will change; 10 won't.
    """
    raise NotImplementedError


# ===========================================================================
# Must-have 2 — refuses instead of hallucinating
# ===========================================================================

def test_out_of_scope_question_is_refused():
    """TODO 2: ask "What is the CEO's home address?" and assert the refusal
            string comes back — and that no source is cited for it.

    This is the single most important behaviour in the product. The mentor
    guide calls silent hallucination the thing to stamp out; this is the test
    that keeps it stamped out.
    """
    raise NotImplementedError


def test_plausible_sounding_out_of_scope_is_refused():
    """Harder case: a question that SOUNDS internal but isn't in the corpus,
    e.g. "What's our policy on remote work from abroad?"

    TODO 3: assert it refuses rather than assembling something plausible from
            adjacent chunks. If this one fails, that's a real finding — write it
            up in RESULTS.md rather than deleting the test.
    """
    raise NotImplementedError


# ===========================================================================
# Must-have 3 — conversational memory
# ===========================================================================

def test_two_turn_follow_up_resolves_pronoun():
    """The behaviour most likely to break silently when the app is mis-wired.

    TODO 4: in ONE session, ask:
              1. "How much PTO do I get?"
              2. "Can I carry it over to next year?"

    Assert the second answer mentions the 5-day carry-over cap, without the
    word "PTO" appearing in the second question. If the history node isn't wired,
    this fails — which is the point.
    """
    raise NotImplementedError


def test_sessions_are_isolated():
    """TODO 5: ask turn 1 in session "user-a". Then ask "Can I carry it over?"
            in session "user-b".

    Assert session B does NOT resolve the pronoun — it should refuse, ask for
    clarification, or answer something unrelated. It must not inherit A's context.

    Claiming isolation isn't enough. Demonstrate it.
    """
    raise NotImplementedError


# ===========================================================================
# Must-have 5 — the index is persisted, not rebuilt
# ===========================================================================

def test_warm_start_does_not_reembed(tmp_path):
    """TODO 6: build the store once into a temp dir, then build again and assert
            the second call loads rather than embeds.

    Time both. Put the two numbers in COST.md — a warm start should be
    dramatically faster, and that difference is your first real cost saving.
    """
    raise NotImplementedError


# ===========================================================================
# Agentic behaviour — does the self-correction loop actually fire?
# ===========================================================================

def test_awkward_query_triggers_rewrite_loop():
    """Week 1's Task 8 asked you to show this once. Make it a repeatable test.

    TODO 7: ask the deliberately awkward "time off carry rules?" and capture the
            node path.

    Assert `rewrite_query` appears in the path — OR, if it reliably doesn't,
    mark this xfail and write up WHY in RESULTS.md. A doc grader that's too
    permissive to ever trigger a rewrite is a genuine finding, and reporting it
    honestly is worth more than a passing test.
    """
    raise NotImplementedError
