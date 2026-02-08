"""挨拶モジュール。基本的な挨拶機能を提供する。"""


def greet(name: str) -> str:
    """指定された名前に対する挨拶メッセージを返す。

    Args:
        name: 挨拶する相手の名前

    Returns:
        挨拶メッセージの文字列
    """
    return f"こんにちは、{name}さん！"


def farewell(name: str) -> str:
    """指定された名前に対する別れのメッセージを返す。

    Args:
        name: 別れを告げる相手の名前

    Returns:
        別れのメッセージの文字列
    """
    return f"さようなら、{name}さん！"


if __name__ == "__main__":
    print(greet("世界"))
