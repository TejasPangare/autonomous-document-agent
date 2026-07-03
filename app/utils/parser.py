import json
import re


def parse_json(text: str):

    text = re.sub(r"```json", "", text, flags=re.IGNORECASE)
    text = text.replace("```", "").strip()

    return json.loads(text)