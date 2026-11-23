"""Спостерігач (Observer) — підписка на курс валют."""
from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, currency: str, rate: float) -> None: ...


class ExchangeRates:
    """Суб'єкт: сповіщає всіх підписників про зміни."""

    def __init__(self) -> None:
        self._observers: list[Observer] = []
        self._rates: dict[str, float] = {}

    def subscribe(self, observer: Observer) -> None:
        self._observers.append(observer)

    def unsubscribe(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def set_rate(self, currency: str, rate: float) -> None:
        self._rates[currency] = rate
        for observer in self._observers:
            observer.update(currency, rate)


class MobileApp(Observer):
    def update(self, currency: str, rate: float) -> None:
        print(f"[Мобільний застосунок] {currency} = {rate} грн")


class EmailSubscriber(Observer):
    def __init__(self, email: str) -> None:
        self.email = email

    def update(self, currency: str, rate: float) -> None:
        print(f"[Лист для {self.email}] Курс {currency} змінився: {rate} грн")


if __name__ == "__main__":
    rates = ExchangeRates()
    app = MobileApp()
    mail = EmailSubscriber("student@example.com")

    rates.subscribe(app)
    rates.subscribe(mail)
    rates.set_rate("USD", 41.5)

    print("--- Користувач відписався від email ---")
    rates.unsubscribe(mail)
    rates.set_rate("EUR", 44.2)
