"""変換モジュール。単位変換や文字列変換の機能を提供する。"""


def celsius_to_fahrenheit(celsius: float) -> float:
    """摂氏温度を華氏温度に変換する。

    Args:
        celsius: 摂氏温度

    Returns:
        華氏温度
    """
    return celsius * 9 / 5 + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """華氏温度を摂氏温度に変換する。

    Args:
        fahrenheit: 華氏温度

    Returns:
        摂氏温度
    """
    return (fahrenheit - 32) * 5 / 9


def km_to_miles(km: float) -> float:
    """キロメートルをマイルに変換する。

    Args:
        km: キロメートル

    Returns:
        マイル
    """
    return km * 0.621371


def miles_to_km(miles: float) -> float:
    """マイルをキロメートルに変換する。

    Args:
        miles: マイル

    Returns:
        キロメートル
    """
    return miles / 0.621371


def to_snake_case(text: str) -> str:
    """文字列をスネークケースに変換する。

    Args:
        text: 変換対象の文字列（スペース区切りまたはキャメルケース）

    Returns:
        スネークケースに変換された文字列
    """
    import re

    # キャメルケースをスペース区切りに変換
    s = re.sub(r"(?<=[a-z])(?=[A-Z])", " ", text)
    # スペースやハイフンをアンダースコアに変換して小文字化
    return re.sub(r"[\s\-]+", "_", s).lower()


def to_camel_case(text: str) -> str:
    """文字列をキャメルケース（PascalCase）に変換する。

    Args:
        text: 変換対象の文字列（スネークケースまたはスペース区切り）

    Returns:
        キャメルケースに変換された文字列
    """
    words = text.replace("-", " ").replace("_", " ").split()
    return "".join(word.capitalize() for word in words)


if __name__ == "__main__":
    print(f"100°C = {celsius_to_fahrenheit(100)}°F")
    print(f"42km = {km_to_miles(42):.2f} miles")
    print(f"hello world -> {to_snake_case('hello world')}")
    print(f"hello_world -> {to_camel_case('hello_world')}")
