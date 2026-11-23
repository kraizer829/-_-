"""Декоратор (Decorator) — кава з добавками."""
from abc import ABC, abstractmethod


class Coffee(ABC):
    @abstractmethod
    def cost(self) -> float: ...

    @abstractmethod
    def description(self) -> str: ...


class Espresso(Coffee):
    def cost(self) -> float:
        return 50.0

    def description(self) -> str:
        return "Еспресо"


class CoffeeDecorator(Coffee):
    def __init__(self, coffee: Coffee) -> None:
        self._coffee = coffee

    def cost(self) -> float:
        return self._coffee.cost()

    def description(self) -> str:
        return self._coffee.description()


class Milk(CoffeeDecorator):
    def cost(self) -> float:
        return self._coffee.cost() + 10

    def description(self) -> str:
        return self._coffee.description() + " + молоко"


class Sugar(CoffeeDecorator):
    def cost(self) -> float:
        return self._coffee.cost() + 5

    def description(self) -> str:
        return self._coffee.description() + " + цукор"


class Syrup(CoffeeDecorator):
    def cost(self) -> float:
        return self._coffee.cost() + 15

    def description(self) -> str:
        return self._coffee.description() + " + сироп"


if __name__ == "__main__":
    order = Syrup(Milk(Sugar(Espresso())))
    print(f"{order.description()} — {order.cost()} грн")
