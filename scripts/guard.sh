#!/bin/bash
# PreToolUse(Bash) hook: 危険なコマンドをブロックする
# stdin から JSON を受け取り、tool_input.command を検査する

set -euo pipefail

INPUT=$(cat)
COMMAND=$(echo "$INPUT" | python3 -c "import sys,json; print(json.load(sys.stdin).get('tool_input',{}).get('command',''))" 2>/dev/null || echo "")

# 危険なパターンを定義
DANGEROUS_PATTERNS=(
  "rm -rf /"
  "rm -rf /*"
  "mkfs"
  "dd if="
  ":(){:|:&};:"
  "chmod -R 777 /"
  "curl.*|.*bash"
  "wget.*|.*bash"
  "sudo rm"
)

for pattern in "${DANGEROUS_PATTERNS[@]}"; do
  if echo "$COMMAND" | grep -qE "$pattern"; then
    echo '{"error": "ブロック: 危険なコマンドが検出されました — '"$pattern"'"}'
    exit 2
  fi
done

exit 0
