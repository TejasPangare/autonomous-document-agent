import os
from dotenv import load_dotenv

load_dotenv()

class Settings:

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

    LLM_PROVIDER = os.getenv("LLM_PROVIDER", "groq")


settings = Settings()