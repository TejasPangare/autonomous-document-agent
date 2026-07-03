from groq import Groq

from app.config import settings

client = Groq(
    api_key=settings.GROQ_API_KEY
)

MODEL = "llama-3.3-70b-versatile"

def invoke(prompt: str) -> str:
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3
    )

    return response.choices[0].message.content