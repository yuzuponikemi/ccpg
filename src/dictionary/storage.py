"""辞書データの永続化を担当するモジュール。"""

from __future__ import annotations

import json
from pathlib import Path

from .models import DictEntry

DEFAULT_DATA_PATH = Path(__file__).parent.parent.parent / "data" / "dictionary.json"


def load_entries(path: Path | None = None) -> list[DictEntry]:
    """辞書データファイルからエントリを読み込む。

    Args:
        path: データファイルのパス。None の場合はデフォルトパスを使用

    Returns:
        辞書エントリのリスト
    """
    data_path = path or DEFAULT_DATA_PATH
    if not data_path.exists():
        return []
    with open(data_path, encoding="utf-8") as f:
        data = json.load(f)
    return [DictEntry.from_dict(entry) for entry in data]


def save_entries(entries: list[DictEntry], path: Path | None = None) -> None:
    """辞書エントリをデータファイルに保存する。

    Args:
        entries: 保存する辞書エントリのリスト
        path: データファイルのパス。None の場合はデフォルトパスを使用
    """
    data_path = path or DEFAULT_DATA_PATH
    data_path.parent.mkdir(parents=True, exist_ok=True)
    with open(data_path, "w", encoding="utf-8") as f:
        json.dump(
            [entry.to_dict() for entry in entries],
            f,
            ensure_ascii=False,
            indent=2,
        )


def add_entry(entry: DictEntry, path: Path | None = None) -> None:
    """辞書に新しいエントリを追加する。

    Args:
        entry: 追加するエントリ
        path: データファイルのパス
    """
    entries = load_entries(path)
    entries.append(entry)
    save_entries(entries, path)
