from fastapi import APIRouter, Query
from app.services.store import search_chunks
import ollama

router = APIRouter()


@router.post("/")
async def query_docs(query: str = Query(...)):
    results = search_chunks(query)

    if not results:
        return {
            "answer": "No relevant information found.",
            "sources": []
        }

    # Build context
    context = "\n\n".join([r["text"] for r in results])

    # 🔥 Improved prompt
    prompt = f"""
You are an AI assistant that answers questions ONLY from the given context.

Rules:
- Extract exact answers if present
- If it's a list (like skills), format properly
- Do NOT say "I don't know" if answer exists
- Be concise

Context:
{context}

Question:
{query}

Answer:
"""

    # Call Ollama (phi3)
    response = ollama.chat(
        model="phi3",
        messages=[{"role": "user", "content": prompt}]
    )

    answer = response["message"]["content"]

    # Clean sources
    sources = [
        {
            "source": r["source"],
            "page": r["page"]
        }
        for r in results
    ]

    return {
        "answer": answer.strip(),
        "sources": sources
    }