from app.llm.factory import invoke
from app.prompts.reviewer import REVIEWER_PROMPT
import json
from app.models import GeneratedDocument
from app.utils.parser import parse_json


class ReviewerTool:

    def review(self, document: str):

        prompt = REVIEWER_PROMPT.format(
            document=json.dumps(
                document.model_dump(),
                indent=2
            )
        )

        response = invoke(prompt)

        reviewed_document = parse_json(response)

        return GeneratedDocument(**reviewed_document)

    