"""Посередник (Mediator) — чат-кімната."""
from __future__ import annotations


class ChatRoom:
    """Посередник: учасники спілкуються лише через нього."""

    def __init__(self) -> None:
        self._users: list[User] = []

    def register(self, user: "User") -> None:
        self._users.append(user)
        user.room = self

    def send(self, message: str, sender: "User") -> None:
        for user in self._users:
            if user is not sender:
                user.receive(message, sender)


class User:
    def __init__(self, name: str) -> None:
        self.name = name
        self.room: ChatRoom | None = None

    def say(self, message: str) -> None:
        print(f"{self.name} пише: {message}")
        if self.room:
            self.room.send(message, self)

    def receive(self, message: str, sender: "User") -> None:
        print(f"  → {self.name} отримав від {sender.name}: {message}")


if __name__ == "__main__":
    room = ChatRoom()
    anna, ivan, olena = User("Анна"), User("Іван"), User("Олена")
    for user in (anna, ivan, olena):
        room.register(user)

    anna.say("Всім привіт!")
    ivan.say("Привіт, Анно!")
