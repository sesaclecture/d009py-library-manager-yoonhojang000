from __future__ import annotations
from typing import Iterable, List
from library.models.book import Book
from library.services.base_service import BaseService

class LibraryService(BaseService):
    def __init__(self) -> None:
        # 내부 상태를 캡슐화하기 위해 _books 리스트 초기화
        self._books: List[Book] = []

    def add_book(self, book: Book) -> None:
        self._books.append(book)

    def remove_book(self, title: str) -> None:
        # 제목이 일치하는 책 찾기
        for i, book in enumerate(self._books):
            if book.title == title:
                del self._books[i]
                return
        raise ValueError(f"Title '{title}' not found in library.")

    def list_books(self) -> Iterable[Book]:
        # 원본 보호를 위해 복사본 반환
        return self._books[:]

    def find_book(self, title: str) -> Book:
        for book in self._books:
            if book.title == title:
                return book
        raise ValueError(f"Title '{title}' not found in library.")