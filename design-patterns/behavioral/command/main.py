"""Команда (Command) — текстовий редактор зі скасуванням дій."""
from abc import ABC, abstractmethod


# --- Отримувач -------------------------------------------------------------
class Editor:
    def __init__(self) -> None:
        self.text = ""


# --- Команди ---------------------------------------------------------------
class Command(ABC):
    @abstractmethod
    def execute(self) -> None: ...

    @abstractmethod
    def undo(self) -> None: ...


class AppendCommand(Command):
    def __init__(self, editor: Editor, text: str) -> None:
        self.editor, self.text = editor, text

    def execute(self) -> None:
        self.editor.text += self.text

    def undo(self) -> None:
        self.editor.text = self.editor.text[: -len(self.text)]


class UppercaseCommand(Command):
    def __init__(self, editor: Editor) -> None:
        self.editor = editor
        self._backup = ""

    def execute(self) -> None:
        self._backup = self.editor.text
        self.editor.text = self.editor.text.upper()

    def undo(self) -> None:
        self.editor.text = self._backup


# --- Ініціатор (інвокер) ---------------------------------------------------
class Invoker:
    def __init__(self) -> None:
        self._history: list[Command] = []

    def run(self, command: Command) -> None:
        command.execute()
        self._history.append(command)

    def undo(self) -> None:
        if self._history:
            self._history.pop().undo()


if __name__ == "__main__":
    editor = Editor()
    invoker = Invoker()

    invoker.run(AppendCommand(editor, "Привіт"))
    invoker.run(AppendCommand(editor, ", світе"))
    print(editor.text)

    invoker.run(UppercaseCommand(editor))
    print(editor.text)

    invoker.undo()
    print("Після undo:", editor.text)
    invoker.undo()
    print("Після undo:", editor.text)
