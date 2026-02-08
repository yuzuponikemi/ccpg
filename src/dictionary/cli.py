"""和英辞書 CLI。コマンドラインから辞書の検索・登録を行う。"""

from __future__ import annotations

import argparse
import sys

from .models import DictEntry
from .search import search
from .storage import add_entry, load_entries


def format_entry(entry: DictEntry) -> str:
    """エントリを表示用にフォーマットする。

    Args:
        entry: フォーマット対象のエントリ

    Returns:
        フォーマットされた文字列
    """
    lines = [f"  {entry.japanese} ({entry.reading}) — {entry.english}"]
    if entry.tags:
        lines[0] += f"  [{', '.join(entry.tags)}]"
    for example in entry.examples:
        lines.append(f"    例: {example}")
    return "\n".join(lines)


def cmd_search(args: argparse.Namespace) -> None:
    """検索コマンドを実行する。

    Args:
        args: コマンドライン引数
    """
    results = search(args.query)
    if not results:
        print(f"「{args.query}」に該当するエントリが見つかりません。")
        return
    print(f"検索結果: {len(results)} 件")
    for entry in results:
        print(format_entry(entry))


def cmd_add(args: argparse.Namespace) -> None:
    """追加コマンドを実行する。

    Args:
        args: コマンドライン引数
    """
    entry = DictEntry(
        japanese=args.japanese,
        english=args.english,
        reading=args.reading or "",
        tags=args.tags.split(",") if args.tags else [],
    )
    add_entry(entry)
    print(f"追加しました: {entry.japanese} — {entry.english}")


def cmd_list(args: argparse.Namespace) -> None:
    """一覧コマンドを実行する。

    Args:
        args: コマンドライン引数
    """
    entries = load_entries()
    if not entries:
        print("辞書にエントリがありません。")
        return
    print(f"全 {len(entries)} 件:")
    for entry in entries:
        print(format_entry(entry))


def main(argv: list[str] | None = None) -> None:
    """CLI のメインエントリポイント。

    Args:
        argv: コマンドライン引数。None の場合は sys.argv を使用
    """
    parser = argparse.ArgumentParser(description="和英辞書 CLI")
    subparsers = parser.add_subparsers(dest="command", help="サブコマンド")

    # search
    p_search = subparsers.add_parser("search", help="辞書を検索する")
    p_search.add_argument("query", help="検索文字列")
    p_search.set_defaults(func=cmd_search)

    # add
    p_add = subparsers.add_parser("add", help="エントリを追加する")
    p_add.add_argument("japanese", help="日本語")
    p_add.add_argument("english", help="英語")
    p_add.add_argument("--reading", help="読み（ひらがな）")
    p_add.add_argument("--tags", help="タグ（カンマ区切り）")
    p_add.set_defaults(func=cmd_add)

    # list
    p_list = subparsers.add_parser("list", help="全エントリを表示する")
    p_list.set_defaults(func=cmd_list)

    args = parser.parse_args(argv)
    if not args.command:
        parser.print_help()
        sys.exit(1)
    args.func(args)


if __name__ == "__main__":
    main()
