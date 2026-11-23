"""Стан (State) — замовлення в інтернет-магазині."""
from __future__ import annotations

from abc import ABC, abstractmethod


class OrderState(ABC):
    @abstractmethod
    def next(self, order: "Order") -> None: ...

    @abstractmethod
    def cancel(self, order: "Order") -> None: ...

    @abstractmethod
    def name(self) -> str: ...


class NewState(OrderState):
    def next(self, order: "Order") -> None:
        order.state = PaidState()

    def cancel(self, order: "Order") -> None:
        order.state = CancelledState()

    def name(self) -> str:
        return "Нове"


class PaidState(OrderState):
    def next(self, order: "Order") -> None:
        order.state = ShippedState()

    def cancel(self, order: "Order") -> None:
        print("  (кошти буде повернено)")
        order.state = CancelledState()

    def name(self) -> str:
        return "Оплачене"


class ShippedState(OrderState):
    def next(self, order: "Order") -> None:
        order.state = DeliveredState()

    def cancel(self, order: "Order") -> None:
        print("  Не можна скасувати: замовлення вже відправлено")

    def name(self) -> str:
        return "Відправлене"


class DeliveredState(OrderState):
    def next(self, order: "Order") -> None:
        print("  Замовлення вже доставлено")

    def cancel(self, order: "Order") -> None:
        print("  Не можна скасувати доставлене замовлення")

    def name(self) -> str:
        return "Доставлене"


class CancelledState(OrderState):
    def next(self, order: "Order") -> None:
        print("  Скасоване замовлення не можна обробляти")

    def cancel(self, order: "Order") -> None:
        print("  Замовлення вже скасоване")

    def name(self) -> str:
        return "Скасоване"


class Order:
    def __init__(self) -> None:
        self.state: OrderState = NewState()

    def next(self) -> None:
        self.state.next(self)

    def cancel(self) -> None:
        self.state.cancel(self)

    def show(self) -> None:
        print(f"Статус: {self.state.name()}")


if __name__ == "__main__":
    order = Order()
    order.show()
    for _ in range(3):
        order.next()
        order.show()

    print("Спроба скасувати:")
    order.cancel()

    other = Order()
    other.next()
    other.cancel()
    other.show()
