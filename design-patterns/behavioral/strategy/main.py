"""Стратегія (Strategy) — способи розрахунку вартості доставки."""
from abc import ABC, abstractmethod


class DeliveryStrategy(ABC):
    @abstractmethod
    def calculate(self, weight_kg: float, distance_km: float) -> float: ...


class CourierDelivery(DeliveryStrategy):
    def calculate(self, weight_kg: float, distance_km: float) -> float:
        return 100 + weight_kg * 10 + distance_km * 2


class PostDelivery(DeliveryStrategy):
    def calculate(self, weight_kg: float, distance_km: float) -> float:
        return 40 + weight_kg * 5 + distance_km * 0.5


class PickupDelivery(DeliveryStrategy):
    def calculate(self, weight_kg: float, distance_km: float) -> float:
        return 0.0


class Order:
    def __init__(self, weight_kg: float, distance_km: float,
                 strategy: DeliveryStrategy) -> None:
        self.weight_kg = weight_kg
        self.distance_km = distance_km
        self._strategy = strategy

    def set_strategy(self, strategy: DeliveryStrategy) -> None:
        self._strategy = strategy

    def delivery_cost(self) -> float:
        return self._strategy.calculate(self.weight_kg, self.distance_km)


if __name__ == "__main__":
    order = Order(weight_kg=3, distance_km=50, strategy=CourierDelivery())
    print(f"Кур'єр:   {order.delivery_cost():.2f} грн")

    order.set_strategy(PostDelivery())
    print(f"Пошта:    {order.delivery_cost():.2f} грн")

    order.set_strategy(PickupDelivery())
    print(f"Самовивіз: {order.delivery_cost():.2f} грн")
