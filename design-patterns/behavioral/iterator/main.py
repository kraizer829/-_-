"""Ітератор (Iterator) — власна колекція з різними способами обходу."""
from collections.abc import Iterator


class BookShelf:
    def __init__(self) -> None:
        self._books: list[str] = []

    def add(self, title: str) -> None:
        self._books.append(title)

    def __iter__(self) -> Iterator[str]:
        return ForwardIterator(self._books)

    def reversed(self) -> Iterator[str]:
        return ReverseIterator(self._books)


class ForwardIterator:
    def __init__(self, items: list[str]) -> None:
        self._items = items
        self._index = 0

    def __iter__(self) -> "ForwardIterator":
        return self

    def __next__(self) -> str:
        if self._index >= len(self._items):
            raise StopIteration
        item = self._items[self._index]
        self._index += 1
        return item


class ReverseIterator:
    def __init__(self, items: list[str]) -> None:
        self._items = items
        self._index = len(items) - 1

    def __iter__(self) -> "ReverseIterator":
        return self

    def __next__(self) -> str:
        if self._index < 0:
            raise StopIteration
        item = self._items[self._index]
        self._index -= 1
        return item


if __name__ == "__main__":
    shelf = BookShelf()
    for title in ("Кобзар", "Тіні забутих предків", "Intermezzo"):
        shelf.add(title)

    print("Прямий обхід:")
    for book in shelf:
        print(" -", book)

    print("Зворотний обхід:")
    for book in shelf.reversed():
        print(" -", book)
