# app/main.py
from fastapi import FastAPI, HTTPException
from app.models import SystemPromptIn, UserPromptIn, EvaluateIn, EvaluateOut
from app.config import settings
from app.storage import save_system_prompt, save_user_prompt, get_prompt_by_id
from app.evaluator import evaluate_pair

app = FastAPI(title="Project2 - Prompt Battle", version="1.0")

@app.get("/")
def home():
    return {"status": "ok", "message": "Project2 Prompt Battle API running."}

@app.post("/system")
def post_system(payload: SystemPromptIn):
    # verify secret
    if payload.secret != settings.SECRET_KEY:
        raise HTTPException(status_code=403, detail="Invalid secret")
    save_system_prompt(payload)
    return {"status": "saved", "student_id": payload.student_id}

@app.post("/user")
def post_user(payload: UserPromptIn):
    if payload.secret != settings.SECRET_KEY:
        raise HTTPException(status_code=403, detail="Invalid secret")
    save_user_prompt(payload)
    return {"status": "saved", "student_id": payload.student_id}

@app.post("/evaluate", response_model=EvaluateOut)
def post_evaluate(payload: EvaluateIn):
    # verify secret
    if payload.secret != settings.SECRET_KEY:
        raise HTTPException(status_code=403, detail="Invalid secret")

    # fetch stored prompts
    system = get_prompt_by_id(payload.system_student_id, kind="system")
    user = get_prompt_by_id(payload.user_student_id, kind="user")

    if system is None:
        raise HTTPException(status_code=404, detail="System prompt not found")
    if user is None:
        raise HTTPException(status_code=404, detail="User prompt not found")

    # evaluate (simulate or prepare payload)
    result = evaluate_pair(system_prompt=system["system_prompt"],
                           user_prompt=user["user_prompt"],
                           simulate=payload.simulate,
                           model_name=payload.model_name)
    return result
