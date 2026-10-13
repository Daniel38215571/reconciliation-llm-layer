# Reconciliation LLM Layer

> **Thesis:** In a regulated industry, an LLM should never own a number. This layer reads structured output from the reconciliation engine and produces plain-English narration — constrained to the facts the input proves.

A traceability-constrained LLM layer that sits on top of the reconciliation engine. The engine computes. The LLM narrates. Every claim in the output maps back to a field in the input JSON.

## Status

**Working locally.** Core pipeline runs end-to-end. FastAPI wrapper included. Not yet deployed.

## What works today

- `build_context()` — transforms a `ReconciliationSummary` into a labeled text block
- `build_user_prompt()` — constructs the user prompt from the context
- `explain_summary()` — calls Gemini with a system prompt that forbids inventing facts
- `POST /explain` — FastAPI endpoint accepting a summary, returning narration
- `GET /health` — liveness check

## Design Principle

**Traceability before intelligence.**

Every number in the LLM output traces to a field in the input JSON. The LLM is not allowed to invent numbers, statuses, or categories. If the input doesn't say it, the narration doesn't say it.

## Architecture

- `llm/schemas.py` — Pydantic models matching reconciliation engine output
- `llm/context.py` — transforms summary into a labeled text block
- `llm/prompt.py` — system and user prompt templates
- `llm/client.py` — Gemini API call, reads `GEMINI_API_KEY` from environment
- `main.py` — FastAPI wrapper exposing `/explain` and `/health`

The LLM never sees individual transactions. Only aggregate summaries.

## Stack

- Python 3.10+
- Google Gemini (gemini-3.0-flash)
- Pydantic v2
- FastAPI, Uvicorn

## What this demonstrates

- **Traceability as architecture** — the LLM cannot narrate what the input doesn't contain
- **Separation of concerns** — context, prompt, and API call are independently testable
- **Regulated-domain awareness** — aggregate-only inputs, no per-customer data in prompts
- **Structured I/O** — Pydantic-validated schemas on both sides

## What this is not

- Not a replacement for the reconciliation engine. It reads its output.
- Not a general-purpose LLM. Prompt and schema are specific to reconciliation.
- Not deployed yet. Render deployment is next.
- Not tested with a judged test set. That's the next milestone.

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env
# edit .env, set GEMINI_API_KEY
