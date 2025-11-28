# app/storage.py
import json
from pathlib import Path
from typing import Optional, Dict
from threading import Lock
from datetime import datetime

DATA_FILE = Path(__file__).resolve().parent.parent / "prompts_store.json"
_LOCK = Lock()

# ensure file exists
if not DATA_FILE.exists():
    DATA_FILE.write_text(json.dumps({"system": {}, "user": {}}))

def _load() -> Dict:
    with _LOCK:
        return json.loads(DATA_FILE.read_text())

def _save(data: Dict):
    with _LOCK:
        DATA_FILE.write_text(json.dumps(data, indent=2))

def save_system_prompt(obj) -> None:
    data = _load()
    data["system"][obj.student_id] = {
        "student_id": obj.student_id,
        "system_prompt": obj.system_prompt,
        "created_at": datetime.utcnow().isoformat()
    }
    _save(data)

def save_user_prompt(obj) -> None:
    data = _load()
    data["user"][obj.student_id] = {
        "student_id": obj.student_id,
        "user_prompt": obj.user_prompt,
        "created_at": datetime.utcnow().isoformat()
    }
    _save(data)

def get_prompt_by_id(student_id: str, kind: str = "system") -> Optional[Dict]:
    data = _load()
    return data.get(kind, {}).get(student_id)
