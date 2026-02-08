---
description: テンプレートから新しいPythonモジュールを生成する
user-invocable: true
---

# 新規モジュール生成スキル

`$ARGUMENTS` を元に新しい Python モジュールを `src/` 配下に作成します。

## 手順

1. `$ARGUMENTS` からモジュール名と説明を解析する（形式: `<モジュール名> <説明>`）
2. このスキルと同じディレクトリにある `template.py` を読み込む
3. テンプレート内のプレースホルダを置換してモジュールを生成する
4. 対応するテストファイルを `tests/` に生成する
5. テストを実行して通ることを確認する

## プレースホルダ

- `{{MODULE_NAME}}` — モジュール名（snake_case）
- `{{MODULE_DOC}}` — モジュールの docstring（日本語）
- `{{CLASS_NAME}}` — クラス名（PascalCase、モジュール名から変換）
