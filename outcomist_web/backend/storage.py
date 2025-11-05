import json
from pathlib import Path
from typing import Optional
from .models import Session


class SessionStorage:
    def __init__(self, data_dir: str = "data/sessions"):
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(parents=True, exist_ok=True)

    def _get_path(self, session_id: str) -> Path:
        return self.data_dir / f"{session_id}.json"

    def save(self, session: Session) -> None:
        path = self._get_path(session.session_id)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(session.model_dump(mode="json"), f, indent=2, ensure_ascii=False)

    def load(self, session_id: str) -> Optional[Session]:
        path = self._get_path(session_id)
        if not path.exists():
            return None

        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return Session(**data)

    def exists(self, session_id: str) -> bool:
        return self._get_path(session_id).exists()
