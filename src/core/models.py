from pydantic import BaseModel, Field
from typing import List

class Task(BaseModel):
    id: str = Field(..., description="Unique identifier for the task.")
    title: str = Field(..., description="Short title of the task.")
    description: str = Field(..., description="Detailed description of what needs to be researched or analyzed.")
    dependencies: List[str] = Field(default_factory=list, description="List of task IDs that must be completed before this task.")

class ExecutionPlan(BaseModel):
    objective: str = Field(..., description="The overall business objective.")
    tasks: List[Task] = Field(..., description="List of tasks required to achieve the objective.")

class TaskResult(BaseModel):
    task_id: str = Field(..., description="The ID of the task this result belongs to.")
    findings: str = Field(..., description="The detailed findings and intelligence gathered for this task.")
    sources_used: List[str] = Field(default_factory=list, description="List of sources or queries used during execution.")
