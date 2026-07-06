import json
from urllib import response
from app.models import ExecutionPlan
from app.utils.parser import parse_json

from app.llm.factory import invoke
from app.prompts.planner import PLANNER_PROMPT


class Planner:

    @staticmethod
    def create_plan(user_request: str):

        prompt = f"""
                {PLANNER_PROMPT}
                User Request:
                {user_request}
                """

        response = invoke(prompt)
        # print("Raw Response:", response)


        try:
            plan = parse_json(response)
            normalized_tasks = []

            for i, task in enumerate(plan["tasks"], start=1):
            
                if isinstance(task, str):
                    normalized_tasks.append({
                        "task_id": i,
                        "title": task,
                        "description": ""
                    })

                else:
                    normalized_tasks.append({
                        "task_id": int(task.get("task_id", i)),
                        "title": task.get("title", ""),
                        "description": task.get("description", "")
                    })

            plan["tasks"] = normalized_tasks
            # print("Normalized Plan:", ExecutionPlan(**plan))
            return ExecutionPlan(**plan)

        except Exception as e:

            print(f"Error: {e}")
            return {
                "document_type": "Business Document",
                "assumptions": [
                    "Used default assumptions because plan parsing failed."
                ],
                "tasks": [
                    "Analyze request",
                    "Create outline",
                    "Generate document",
                    "Review document",
                    "Generate Word file"
                ]
            }