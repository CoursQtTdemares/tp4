from pathlib import Path


def load_styles(file_path: Path) -> str:
    return file_path.read_text()
