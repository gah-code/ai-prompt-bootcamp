from datetime import datetime
from typing import Iterable, Optional


def basic_prompt_template(question: str, tags: Optional[Iterable[str]] = None) -> dict:
    tags_list = list(tags) if tags is not None else []
    prompt = f"Answer the question clearly and concisely:\n\n{question}"
    return {
        "question": question,
        "tags": tags_list,
        "prompt": prompt,
        "created_at": datetime.utcnow().isoformat(timespec="seconds") + "Z",
    }
