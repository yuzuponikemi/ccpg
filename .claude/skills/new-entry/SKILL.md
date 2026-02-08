---
description: 和英辞書に新しいエントリを追加する
user-invocable: true
---

# 辞書エントリ追加スキル

`$ARGUMENTS` を解析して和英辞書に新しいエントリを追加します。

## 引数の形式

```
/new-entry <日本語> <英語> [--reading <読み>] [--tags <タグ>] [--example <例文>]
```

## 手順

1. `$ARGUMENTS` から日本語、英語、読み、タグ、例文を解析する
2. `data/dictionary.json` にエントリを追加する（CLI の `add` コマンドまたは直接ファイル編集）
3. 追加結果を表示する
4. 読みが省略された場合は推測して補完する

## 注意
- `data/` ディレクトリ以外のファイルは変更しない
- JSON の整形（indent=2, ensure_ascii=False）を維持する
