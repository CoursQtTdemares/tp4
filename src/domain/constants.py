from pathlib import Path
from zoneinfo import ZoneInfo

# Paths of the application

WORKSPACE_DIR = Path(__file__).parents[2].resolve()

SRC_DIR = WORKSPACE_DIR / "src"

ICONS_FILE_PATH = WORKSPACE_DIR / "bonhomme-de-neige.png"

STYLES_FILE_PATH = WORKSPACE_DIR / "src" / "styles.css"

PARIS_TZ = ZoneInfo("Europe/Paris")
