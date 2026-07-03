from app.llm.factory import invoke
from app.models import GeneratedDocument
from app.prompts.writer import WRITER_PROMPT
from app.utils.parser import parse_json
import json



class WriterTool:

    def execute(self, request, plan):

        task_list = ""

        for task in plan.tasks:

            
            task_list = json.dumps(
                [task.model_dump() for task in plan.tasks],
                indent=2
            )
            

        # print("Task List:", task_list)
        
        prompt = WRITER_PROMPT.format(
            request=request,
            document_type=plan.document_type,
            assumptions="\n".join(plan.assumptions),
            tasks=task_list,
        )

        response = invoke(prompt)

        document = parse_json(response)

        return GeneratedDocument(**document)