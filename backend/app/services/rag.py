import app.config 
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

def generate_answer(query, context_docs):
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return "I don't know."

    context = "\n\n".join(context_docs)
    if not context.strip():
        return "I don't know."

    client = OpenAI(api_key=api_key)

    prompt = f"""
You are an enterprise assistant.

Rules:
- Answer ONLY from the context.
- If the answer is not in the context, say exactly: I don't know.
- Do not invent details.

Context:
{context}

Question:
{query}
"""

    try:
        response = client.chat.completions.create(
            model="phi3",
            messages=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message.content.strip()
    except Exception:
        return "I don't know."