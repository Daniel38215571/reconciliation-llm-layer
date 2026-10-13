"""FastAPI wrapper around the reconciliation LLM layer."""
from fastapi import FastAPI, HTTPException
from llm.schemas import ReconciliationSummary
from llm.client import explain_summary

app = FastAPI(
    title="Reconciliation LLM Layer",
    description="Traceability-constrained narration over reconciliation output.",
    version="0.1.0",
)


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/explain")
def explain(summary: ReconciliationSummary) -> dict:
    try:
        narration = explain_summary(summary)
    except RuntimeError as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {
        "run_id": summary.run_id,
        "narration": narration,
    }
