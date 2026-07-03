from fastapi import FastAPI

from app.agent.planner import Planner
from app.agent.executor import Executor
from app.models import AgentRequest

app = FastAPI()


@app.post("/agent")
def agent(request: AgentRequest):

    plan = Planner.create_plan(request.request)

    executor = Executor()

    result = executor.execute(
        request=request.request,
        plan=plan
    )

    return {
    "status": "completed",
    "plan": plan,
    "document": result["document"],
    "document_path": result["path"]
}