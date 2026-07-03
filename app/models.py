from typing import List
from pydantic import BaseModel


class AgentRequest(BaseModel):
    request: str


class Task(BaseModel):
    task_id: int
    title: str
    description: str


class ExecutionPlan(BaseModel):
    document_type: str
    assumptions: List[str]
    tasks: List[Task]


class DocumentSection(BaseModel):
    heading: str
    content: str


class GeneratedDocument(BaseModel):
    title: str
    sections: List[DocumentSection]