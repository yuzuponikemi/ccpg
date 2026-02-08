#!/bin/bash
# PostToolUse(Write) hook: Python ファイル書き込み後に構文チェックを行う
# stdin から JSON を受け取り、tool_input.file_path を取得する

set -euo pipefail

INPUT=$(cat)
FILE_PATH=$(echo "$INPUT" | python3 -c "import sys,json; print(json.load(sys.stdin).get('tool_input',{}).get('file_path',''))" 2>/dev/null || echo "")

# Python ファイル以外は無視
if [[ "$FILE_PATH" != *.py ]]; then
  exit 0
fi

# ファイルが存在しない場合は無視
if [[ ! -f "$FILE_PATH" ]]; then
  exit 0
fi

# 構文チェック
if python3 -m py_compile "$FILE_PATH" 2>&1; then
  echo "lint OK: $FILE_PATH"
else
  echo "lint FAILED: $FILE_PATH"
  exit 1
fi
