# CCPG — Claude Code Playground

## プロジェクト概要
Claude Code の主要機能を段階的に学ぶための学習用リポジトリ。

## 言語・ランタイム
- Python 3.11+

## コーディング規約
- **型ヒント必須**: すべての関数に引数・戻り値の型アノテーションを付ける
- **docstring は日本語**: モジュール・クラス・関数の docstring は日本語で記述する
- **テスト**: pytest を使用する
- **インポート順序**: 標準ライブラリ → サードパーティ → ローカル

## コマンド
- テスト実行: `python -m pytest tests/ -v`
- 単一テスト: `python -m pytest tests/test_hello.py -v`
- lint: `python -m py_compile src/*.py`

## ディレクトリ構成
- `src/` — メインのソースコード
- `tests/` — テストコード
- `scripts/` — ユーティリティスクリプト
- `.claude/` — Claude Code の設定ファイル
