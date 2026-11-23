"""Шаблонний метод (Template Method) — обробка файлів із даними."""
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def process(self) -> None:
        """Шаблонний метод: фіксує скелет алгоритму."""
        data = self.read()
        parsed = self.parse(data)
        self.analyze(parsed)
        if self.needs_report():  # «хук»: необов'язковий для перевизначення
            self.report(parsed)

    @abstractmethod
    def read(self) -> str: ...

    @abstractmethod
    def parse(self, raw: str) -> list[int]: ...

    def analyze(self, items: list[int]) -> None:
        print(f"  Сума: {sum(items)}, максимум: {max(items)}")

    def needs_report(self) -> bool:
        return False

    def report(self, items: list[int]) -> None:
        print(f"  Звіт: оброблено {len(items)} значень")


class CsvProcessor(DataProcessor):
    def read(self) -> str:
        print("Читаємо CSV...")
        return "3,7,12,5"

    def parse(self, raw: str) -> list[int]:
        return [int(x) for x in raw.split(",")]


class TextProcessor(DataProcessor):
    def read(self) -> str:
        print("Читаємо TXT...")
        return "10 20 30"

    def parse(self, raw: str) -> list[int]:
        return [int(x) for x in raw.split()]

    def needs_report(self) -> bool:
        return True


if __name__ == "__main__":
    for processor in (CsvProcessor(), TextProcessor()):
        processor.process()
