"""辞書モジュールのテスト。"""

import json
from pathlib import Path

from src.dictionary.models import DictEntry
from src.dictionary.search import search, search_english, search_japanese
from src.dictionary.storage import add_entry, load_entries, save_entries


def _make_entries() -> list[DictEntry]:
    """テスト用のエントリリストを生成する。"""
    return [
        DictEntry(japanese="猫", english="cat", reading="ねこ", tags=["名詞"]),
        DictEntry(japanese="犬", english="dog", reading="いぬ", tags=["名詞"]),
        DictEntry(japanese="食べる", english="eat", reading="たべる", tags=["動詞"]),
    ]


# --- models ---


def test_entry_to_dict() -> None:
    """DictEntry.to_dict が正しい辞書を返すことを検証する。"""
    entry = DictEntry(japanese="猫", english="cat", reading="ねこ")
    d = entry.to_dict()
    assert d["japanese"] == "猫"
    assert d["english"] == "cat"
    assert d["reading"] == "ねこ"


def test_entry_from_dict() -> None:
    """DictEntry.from_dict が正しいインスタンスを返すことを検証する。"""
    data = {"japanese": "猫", "english": "cat", "reading": "ねこ", "tags": ["名詞"]}
    entry = DictEntry.from_dict(data)
    assert entry.japanese == "猫"
    assert entry.tags == ["名詞"]


def test_entry_from_dict_minimal() -> None:
    """最小限のデータから DictEntry を生成できることを検証する。"""
    data = {"japanese": "猫", "english": "cat"}
    entry = DictEntry.from_dict(data)
    assert entry.reading == ""
    assert entry.examples == []
    assert entry.tags == []


# --- search ---


def test_search_japanese() -> None:
    """日本語検索が正しく動作することを検証する。"""
    entries = _make_entries()
    results = search_japanese("猫", entries)
    assert len(results) == 1
    assert results[0].english == "cat"


def test_search_japanese_by_reading() -> None:
    """読みでの検索が正しく動作することを検証する。"""
    entries = _make_entries()
    results = search_japanese("ねこ", entries)
    assert len(results) == 1


def test_search_english() -> None:
    """英語検索が正しく動作することを検証する。"""
    entries = _make_entries()
    results = search_english("cat", entries)
    assert len(results) == 1
    assert results[0].japanese == "猫"


def test_search_english_case_insensitive() -> None:
    """英語検索が大文字小文字を区別しないことを検証する。"""
    entries = _make_entries()
    results = search_english("CAT", entries)
    assert len(results) == 1


def test_search_combined() -> None:
    """統合検索で重複なく結果が返ることを検証する。"""
    entries = _make_entries()
    results = search("猫", entries)
    assert len(results) == 1


def test_search_no_results() -> None:
    """該当なしの場合に空リストが返ることを検証する。"""
    entries = _make_entries()
    results = search("象", entries)
    assert results == []


# --- storage ---


def test_save_and_load(tmp_path: Path) -> None:
    """保存と読み込みが正しく動作することを検証する。"""
    path = tmp_path / "test_dict.json"
    entries = _make_entries()
    save_entries(entries, path)
    loaded = load_entries(path)
    assert len(loaded) == 3
    assert loaded[0].japanese == "猫"


def test_load_nonexistent(tmp_path: Path) -> None:
    """存在しないファイルから読み込むと空リストが返ることを検証する。"""
    path = tmp_path / "nonexistent.json"
    result = load_entries(path)
    assert result == []


def test_add_entry(tmp_path: Path) -> None:
    """add_entry でエントリが追加されることを検証する。"""
    path = tmp_path / "test_dict.json"
    save_entries([], path)
    new_entry = DictEntry(japanese="鳥", english="bird", reading="とり")
    add_entry(new_entry, path)
    entries = load_entries(path)
    assert len(entries) == 1
    assert entries[0].japanese == "鳥"
