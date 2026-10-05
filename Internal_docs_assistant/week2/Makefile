# Week 2 — one-command entry points.
# Copy this to the REPO ROOT: the paths below (tests/, app/, scripts/) are relative
# to it. Task 2 asks you to make `make check` real. The other targets fill in as you go.

.PHONY: help check check-live run run-ui eval cost fmt

help:
	@echo "make check       lint + fast tests   (no API key, must run in < 5s)"
	@echo "make check-live  integration tests   (real API calls, costs money)"
	@echo "make run         start the API       (Task 3)"
	@echo "make run-ui      start the Streamlit UI against the API"
	@echo "make eval        run the LangSmith eval suite (Task 7)"
	@echo "make cost        print the cost report (Task 5)"
	@echo "make fmt         format + autofix lint"

# --- Task 2 ---------------------------------------------------------------
check:
	ruff check .
	pytest tests -m "not live" -q

check-live:
	pytest tests -m live -q

fmt:
	ruff check --fix .
	ruff format .

# --- Task 3 ---------------------------------------------------------------
run:
	uvicorn app.main:app --reload --host $${API_HOST:-0.0.0.0} --port $${API_PORT:-8000}

run-ui:
	streamlit run app/ui.py

# --- Tasks 5 & 7 ----------------------------------------------------------
eval:
	python scripts/run_eval.py

cost:
	python scripts/cost_report.py
