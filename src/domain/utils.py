import json
from pathlib import Path
from typing import TypedDict


def load_styles(file_path: Path) -> str:
    return file_path.read_text()


class Message(TypedDict):
    message: str


def load_messages(file_path: Path) -> list[Message]:
    return json.loads(file_path.read_text())["messages"]


def save_messages(file_path: Path, messages: list[Message]) -> None:
    file_path.write_text(json.dumps({"messages": messages}, indent=4))
