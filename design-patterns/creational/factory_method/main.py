"""Фабричний метод (Factory Method) — логістична компанія."""
from abc import ABC, abstractmethod


# --- Продукт ---------------------------------------------------------------
class Transport(ABC):
    @abstractmethod
    def deliver(self, cargo: str) -> str: ...


class Truck(Transport):
    def deliver(self, cargo: str) -> str:
        return f"Вантажівка везе «{cargo}» по дорозі"


class Ship(Transport):
    def deliver(self, cargo: str) -> str:
        return f"Корабель везе «{cargo}» морем"


# --- Творець ---------------------------------------------------------------
class Logistics(ABC):
    @abstractmethod
    def create_transport(self) -> Transport:
        """Фабричний метод: підкласи самі вирішують, що створювати."""

    def plan_delivery(self, cargo: str) -> str:
        transport = self.create_transport()
        return transport.deliver(cargo)


class RoadLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Truck()


class SeaLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Ship()


if __name__ == "__main__":
    for company in (RoadLogistics(), SeaLogistics()):
        print(company.plan_delivery("ящики з товаром"))
