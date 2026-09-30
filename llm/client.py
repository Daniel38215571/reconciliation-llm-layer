import os
import google.generativeai as genai

from llm.prompt import SYSTEM_PROMPT, build_user_prompt
from llm.context import build_context
from llm.schemas import ReconciliationSummary


GEMINI_MODEL = "gemini-3.8-flash"


def _configure():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("GEMINI_API_KEY not set.")
    genai.configure(api_key=api_key)


def explain_summary(summary: ReconciliationSummary) -> str:
    _configure()
    context = build_context(summary)
    user_prompt = build_user_prompt(context)

    model = genai.GenerativeModel(
        model_name=GEMINI_MODEL,
        system_instruction=SYSTEM_PROMPT,
    )
    response = model.generate_content(user_prompt)
    return response.text
