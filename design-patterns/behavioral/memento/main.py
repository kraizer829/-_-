"""Знімок (Memento) — збереження та відновлення стану редактора."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Memento:
    """Знімок стану. Незмінний, зовні його вміст не змінюють."""
    text: str
    cursor: int


class TextEditor:
    """Творець: створює знімки свого стану й відновлюється з них."""

    def __init__(self) -> None:
        self.text = ""
        self.cursor = 0

    def type(self, words: str) -> None:
        self.text += words
        self.cursor = len(self.text)

    def save(self) -> Memento:
        return Memento(self.text, self.cursor)

    def restore(self, memento: Memento) -> None:
        self.text = memento.text
        self.cursor = memento.cursor

    def __str__(self) -> str:
        return f"«{self.text}» (курсор: {self.cursor})"


class History:
    """Опікун: зберігає знімки, але не заглядає всередину."""

    def __init__(self, editor: TextEditor) -> None:
        self._editor = editor
        self._snapshots: list[Memento] = []

    def backup(self) -> None:
        self._snapshots.append(self._editor.save())

    def undo(self) -> None:
        if self._snapshots:
            self._editor.restore(self._snapshots.pop())


if __name__ == "__main__":
    editor = TextEditor()
    history = History(editor)

    editor.type("Hello")
    history.backup()
    editor.type(", world")
    history.backup()
    editor.type("!!!")
    print("Зараз:    ", editor)

    history.undo()
    print("Undo 1:   ", editor)
    history.undo()
    print("Undo 2:   ", editor)
