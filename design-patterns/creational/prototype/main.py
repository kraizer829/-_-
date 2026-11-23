"""Прототип (Prototype) — клонування шаблонів документів."""
import copy
from abc import ABC, abstractmethod


class Prototype(ABC):
    @abstractmethod
    def clone(self) -> "Prototype": ...


class Document(Prototype):
    def __init__(self, title: str, sections: list[str]) -> None:
        self.title = title
        self.sections = sections

    def clone(self) -> "Document":
        # deepcopy, щоб копія не ділила з оригіналом список розділів
        return copy.deepcopy(self)

    def __str__(self) -> str:
        return f"{self.title}: {', '.join(self.sections)}"


class PrototypeRegistry:
    """Реєстр готових прототипів."""

    def __init__(self) -> None:
        self._items: dict[str, Prototype] = {}

    def register(self, name: str, prototype: Prototype) -> None:
        self._items[name] = prototype

    def create(self, name: str) -> Prototype:
        return self._items[name].clone()


if __name__ == "__main__":
    template = Document("Звіт", ["Вступ", "Основна частина", "Висновки"])

    registry = PrototypeRegistry()
    registry.register("report", template)

    report = registry.create("report")
    report.title = "Звіт з практики"
    report.sections.append("Додатки")

    print("Шаблон:", template)   # не змінився
    print("Копія: ", report)
    print("Це різні об'єкти:", template is not report)
