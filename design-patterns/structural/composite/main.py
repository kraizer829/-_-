"""Компонувальник (Composite) — файли та папки."""
from abc import ABC, abstractmethod


class FileSystemItem(ABC):
    def __init__(self, name: str) -> None:
        self.name = name

    @abstractmethod
    def size(self) -> int: ...

    @abstractmethod
    def show(self, indent: int = 0) -> None: ...


class File(FileSystemItem):
    def __init__(self, name: str, size: int) -> None:
        super().__init__(name)
        self._size = size

    def size(self) -> int:
        return self._size

    def show(self, indent: int = 0) -> None:
        print(" " * indent + f"📄 {self.name} ({self._size} КБ)")


class Folder(FileSystemItem):
    def __init__(self, name: str) -> None:
        super().__init__(name)
        self._children: list[FileSystemItem] = []

    def add(self, item: FileSystemItem) -> "Folder":
        self._children.append(item)
        return self

    def size(self) -> int:
        return sum(child.size() for child in self._children)

    def show(self, indent: int = 0) -> None:
        print(" " * indent + f"📁 {self.name} ({self.size()} КБ)")
        for child in self._children:
            child.show(indent + 4)


if __name__ == "__main__":
    root = Folder("project")
    src = Folder("src").add(File("main.py", 12)).add(File("utils.py", 7))
    docs = Folder("docs").add(File("readme.md", 3))
    root.add(src).add(docs).add(File("LICENSE", 1))

    root.show()
    print("Загальний розмір:", root.size(), "КБ")
