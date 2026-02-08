"""辞書エントリのデータモデル。"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class DictEntry:
    """和英辞書の一エントリを表すデータクラス。

    Args:
        japanese: 日本語の単語
        english: 英語の訳語
        reading: 読み（ひらがな）
        examples: 例文のリスト
        tags: タグのリスト（品詞、分野など）
    """

    japanese: str
    english: str
    reading: str = ""
    examples: list[str] = field(default_factory=list)
    tags: list[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        """辞書形式に変換する。

        Returns:
            エントリの辞書表現
        """
        return {
            "japanese": self.japanese,
            "english": self.english,
            "reading": self.reading,
            "examples": self.examples,
            "tags": self.tags,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "DictEntry":
        """辞書形式からインスタンスを生成する。

        Args:
            data: エントリの辞書表現

        Returns:
            DictEntry インスタンス
        """
        return cls(
            japanese=data["japanese"],
            english=data["english"],
            reading=data.get("reading", ""),
            examples=data.get("examples", []),
            tags=data.get("tags", []),
        )
