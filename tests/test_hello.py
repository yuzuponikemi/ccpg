"""hello モジュールのテスト。"""

from src.hello import farewell, greet


def test_greet_returns_greeting() -> None:
    """greet が正しい挨拶メッセージを返すことを検証する。"""
    assert greet("太郎") == "こんにちは、太郎さん！"


def test_greet_with_english_name() -> None:
    """greet が英語名でも動作することを検証する。"""
    assert greet("Alice") == "こんにちは、Aliceさん！"


def test_farewell_returns_message() -> None:
    """farewell が正しい別れのメッセージを返すことを検証する。"""
    assert farewell("太郎") == "さようなら、太郎さん！"
