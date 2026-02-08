"""計算モジュール。基本的な算術演算を提供する。"""


def add(a: float, b: float) -> float:
    """二つの数値を加算する。

    Args:
        a: 加算される数値
        b: 加算する数値

    Returns:
        a と b の和
    """
    return a + b


def subtract(a: float, b: float) -> float:
    """二つの数値を減算する。

    Args:
        a: 減算される数値
        b: 減算する数値

    Returns:
        a から b を引いた差
    """
    return a - b


def multiply(a: float, b: float) -> float:
    """二つの数値を乗算する。

    Args:
        a: 乗算される数値
        b: 乗算する数値

    Returns:
        a と b の積
    """
    return a * b


def divide(a: float, b: float) -> float:
    """二つの数値を除算する。

    Args:
        a: 除算される数値（被除数）
        b: 除算する数値（除数）

    Returns:
        a を b で割った商

    Raises:
        ZeroDivisionError: b が 0 の場合
    """
    if b == 0:
        raise ZeroDivisionError("0 で割ることはできません")
    return a / b


if __name__ == "__main__":
    print(f"1 + 2 = {add(1, 2)}")
    print(f"10 - 3 = {subtract(10, 3)}")
    print(f"4 * 5 = {multiply(4, 5)}")
    print(f"10 / 3 = {divide(10, 3)}")
