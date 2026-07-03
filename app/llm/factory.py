from app.config import settings

if settings.LLM_PROVIDER == "groq":
    from app.llm.groq import invoke

elif settings.LLM_PROVIDER == "gemini":
    from app.llm.gemini import invoke

else:
    raise Exception("Unsupported LLM")