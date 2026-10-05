"""
Shared pytest fixtures for the Week 2 test suite.

Copy this file (and its siblings) to `tests/` at the repo root.

Two tiers of test live here:
  * fast  — no network, no API key, must finish in < 5s. Runs on every PR.
  * live  — real API calls. Marked @pytest.mark.live, run on demand.

Run them with:
    make check        # fast only  (pytest -m "not live")
    make check-live   # live only  (pytest -m live)
"""

import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))


def pytest_configure(config):
    """Register the `live` marker so pytest doesn't warn about it."""
    config.addinivalue_line(
        "markers", "live: test makes real API calls (costs money, needs keys)"
    )


# ---------------------------------------------------------------------------
# Fake LLM — lets the fast tier exercise real graph code with no network.
# ---------------------------------------------------------------------------
class FakeMessage:
    def __init__(self, content):
        self.content = content


class FakeLLM:
    """Stands in for a chat model.

    `.invoke()` returns a canned message. `.with_structured_output(Schema)`
    returns another FakeLLM that produces instances of that schema, so the
    graders in your graph get a real object back instead of a string.

    Control what it returns per-test:

        llm = FakeLLM(text="20 days of PTO per year.")
        llm.set_structured(RouteDecision, route="retrieve")
    """

    def __init__(self, text="canned answer"):
        self.text = text
        self._schema = None
        self._schema_kwargs = {}
        self.calls = []          # every prompt it was given, for assertions

    def invoke(self, prompt, *args, **kwargs):
        self.calls.append(prompt)
        if self._schema is not None:
            return self._schema(**self._schema_kwargs)
        return FakeMessage(self.text)

    def with_structured_output(self, schema, **_):
        clone = FakeLLM(self.text)
        clone.calls = self.calls          # share the call log
        clone._schema = schema
        clone._schema_kwargs = self._schema_kwargs
        return clone

    def set_structured(self, schema, **kwargs):
        self._schema = schema
        self._schema_kwargs = kwargs
        return self

    # LCEL support: `prompt | llm` needs the right-hand side to be pipeable.
    def __ror__(self, other):
        return _FakeChain(self, other)


class _FakeChain:
    def __init__(self, llm, upstream):
        self.llm = llm
        self.upstream = upstream

    def invoke(self, inputs, *args, **kwargs):
        return self.llm.invoke(str(inputs))


@pytest.fixture
def fake_llm():
    """A FakeLLM you can configure per test."""
    return FakeLLM()


# ---------------------------------------------------------------------------
# Documents & index
# ---------------------------------------------------------------------------
@pytest.fixture
def sample_docs():
    """A handful of Documents that look like the real corpus."""
    from langchain_core.documents import Document

    return [
        Document(
            page_content="Full-time employees accrue 20 days of PTO per year, "
                         "at 1.67 days per month. Up to 5 days carry over.",
            metadata={"source": "employee_handbook.md"},
        ),
        Document(
            page_content="If your laptop is lost or stolen, immediately report "
                         "it to the Security team and file a ticket marked URGENT.",
            metadata={"source": "it_faq.md"},
        ),
        Document(
            page_content="The Warehouse Rover R2 has a maximum payload of 80 kg.",
            metadata={"source": "product_specs.md"},
        ),
    ]


@pytest.fixture
def temp_index_dir(tmp_path):
    """An empty directory standing in for faiss_index/."""
    d = tmp_path / "faiss_index"
    return d


# ---------------------------------------------------------------------------
# TODO 1: add a fixture that returns the compiled graph the APP actually uses.
#         Import it the same way app.py does — that's the whole point, because
#         importing it a different way is exactly the bug you're guarding against.
#
# @pytest.fixture
# def app_graph():
#     ...
# ---------------------------------------------------------------------------
