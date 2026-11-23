"""Ланцюжок обов'язків (Chain of Responsibility) — служба підтримки."""
from __future__ import annotations


class Handler:
    def __init__(self) -> None:
        self._next: Handler | None = None

    def set_next(self, handler: "Handler") -> "Handler":
        self._next = handler
        return handler  # дозволяє будувати ланцюжок: a.set_next(b).set_next(c)

    def handle(self, request: dict) -> str:
        if self._next:
            return self._next.handle(request)
        return "Ніхто не зміг обробити запит"


class Bot(Handler):
    def handle(self, request: dict) -> str:
        if request["level"] == 1:
            return f"Бот: відповів на питання «{request['text']}»"
        return super().handle(request)


class Operator(Handler):
    def handle(self, request: dict) -> str:
        if request["level"] == 2:
            return f"Оператор: розв'язав проблему «{request['text']}»"
        return super().handle(request)


class Manager(Handler):
    def handle(self, request: dict) -> str:
        if request["level"] == 3:
            return f"Менеджер: вирішив скаргу «{request['text']}»"
        return super().handle(request)


if __name__ == "__main__":
    bot = Bot()
    bot.set_next(Operator()).set_next(Manager())

    requests = [
        {"level": 1, "text": "Як змінити пароль?"},
        {"level": 2, "text": "Не проходить платіж"},
        {"level": 3, "text": "Повернення коштів"},
        {"level": 4, "text": "Незрозумілий запит"},
    ]
    for req in requests:
        print(bot.handle(req))
