"""辞書検索モジュール。日本語・英語での検索機能を提供する。"""

from __future__ import annotations

from .models import DictEntry
from .storage import load_entries


def search_japanese(query: str, entries: list[DictEntry] | None = None) -> list[DictEntry]:
    """日本語で辞書を検索する。

    Args:
        query: 検索する日本語文字列
        entries: 検索対象のエントリリスト。None の場合はファイルから読み込む

    Returns:
        マッチしたエントリのリスト
    """
    if entries is None:
        entries = load_entries()
    return [e for e in entries if query in e.japanese or query in e.reading]


def search_english(query: str, entries: list[DictEntry] | None = None) -> list[DictEntry]:
    """英語で辞書を検索する。

    Args:
        query: 検索する英語文字列
        entries: 検索対象のエントリリスト。None の場合はファイルから読み込む

    Returns:
        マッチしたエントリのリスト
    """
    if entries is None:
        entries = load_entries()
    query_lower = query.lower()
    return [e for e in entries if query_lower in e.english.lower()]


def search(query: str, entries: list[DictEntry] | None = None) -> list[DictEntry]:
    """日本語・英語の両方で辞書を検索する。

    Args:
        query: 検索文字列
        entries: 検索対象のエントリリスト。None の場合はファイルから読み込む

    Returns:
        マッチしたエントリのリスト（重複なし）
    """
    if entries is None:
        entries = load_entries()
    ja_results = search_japanese(query, entries)
    en_results = search_english(query, entries)
    # 重複を除去しつつ順序を保持
    seen: set[str] = set()
    results: list[DictEntry] = []
    for entry in ja_results + en_results:
        key = f"{entry.japanese}:{entry.english}"
        if key not in seen:
            seen.add(key)
            results.append(entry)
    return results
