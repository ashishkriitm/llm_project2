# app/models.py
from pydantic import BaseModel, Field
from typing import Optional

class SystemPromptIn(BaseModel):
    student_id: str = Field(..., description="Student identifier")
    secret: str
    system_prompt: str = Field(..., max_length=200)

class UserPromptIn(BaseModel):
    student_id: str = Field(..., description="Student identifier")
    secret: str
    user_prompt: str = Field(..., max_length=200)

class EvaluateIn(BaseModel):
    secret: str
    system_student_id: str
    user_student_id: str
    simulate: bool = True  # if True, server runs a simulated LLM. If False, returns payload for external evaluation
    model_name: Optional[str] = "gpt-5-nano"

class EvaluateOut(BaseModel):
    system_student_id: str
    user_student_id: str
    code_word: str
    model_name: str
    model_output: str
    system_point: int
    user_point: int
    reason: Optional[str] = None
