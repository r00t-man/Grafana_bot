import json
from pathlib import Path


DATA_DIR = Path(__file__).resolve().parent.parent / "data"
FLAGS_PATH = DATA_DIR / "node_flags.json"
DEFAULT_PATH = DATA_DIR / "node_flags.json_temp"


def _ensure_storage():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    if FLAGS_PATH.exists():
        return
    if DEFAULT_PATH.exists():
        FLAGS_PATH.write_text(DEFAULT_PATH.read_text(encoding="utf-8"), encoding="utf-8")
        return
    FLAGS_PATH.write_text("{}", encoding="utf-8")


def _load() -> dict:
    _ensure_storage()
    try:
        data = json.loads(FLAGS_PATH.read_text(encoding="utf-8"))
        return data if isinstance(data, dict) else {}
    except Exception:
        return {}


def _save(data: dict):
    _ensure_storage()
    FLAGS_PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def get_flag(node_name: str) -> str:
    return _load().get(node_name, "")


def set_flag(node_name: str, flag: str):
    data = _load()
    data[node_name] = flag
    _save(data)
