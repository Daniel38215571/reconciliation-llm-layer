# Reconciliation LLM Layer

An LLM explanation layer for the reconciliation engine. Takes a reconciliation summary as JSON, produces a plain-English narration, constrained to only the facts the input proves.

## Design Principle

Traceability before intelligence.

Every number in the LLM output traces to a field in the input JSON. The LLM is not allowed to invent numbers, statuses, or categories.

## How It Works

1. A reconciliation summary arrives as JSON.
2. context.py builds a text block from the JSON.
3. prompt.py constrains the LLM to narrate only what the block proves.
4. client.py calls Google Gemini and returns the explanation.

## Stack

- Python 3.10+
- Google Gemini (gemini-3.8-flash)
- Pydantic v2
- google-generativeai

## Author

Anuoluwapo Daniel Ojo
Software Engineer | Fintech and Payments

- GitHub: github.com/Daniel38215571
- LinkedIn: linkedin.com/in/daniel-ojo-879273197
- Email: ojodaniel38@gmail.com
- Location: Lagos, Nigeria (Remote-ready)

Data x AI x Software. Building systems that prove themselves.
