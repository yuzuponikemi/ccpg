"""{{MODULE_DOC}}"""


class {{CLASS_NAME}}:
    """{{MODULE_DOC}}"""

    def __init__(self) -> None:
        """インスタンスを初期化する。"""
        pass

    def __repr__(self) -> str:
        """オブジェクトの文字列表現を返す。"""
        return f"{self.__class__.__name__}()"


if __name__ == "__main__":
    obj = {{CLASS_NAME}}()
    print(obj)
