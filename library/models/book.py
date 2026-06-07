from __future__ import annotations
from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class Book:
    title: str
    author: str
    year: int

    # 클래스 변수: 모든 객체가 공유
    book_count: int = 0

    def __post_init__(self):
        # 객체가 생성된 후(init 이후) 호출됨
        Book.book_count += 1

    def __str__(self) -> str:
        return f"{self.title} by {self.author} ({self.year})"

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Book":
        return cls(
            title=data.get("title", "Unknown"),
            author=data.get("author", "Unknown"),
            year=data.get("year", 0)
        )