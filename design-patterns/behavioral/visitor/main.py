"""Відвідувач (Visitor) — нові операції над геометричними фігурами."""
import math
from abc import ABC, abstractmethod


# --- Відвідувач ------------------------------------------------------------
class Visitor(ABC):
    @abstractmethod
    def visit_circle(self, circle: "Circle") -> str: ...

    @abstractmethod
    def visit_rectangle(self, rectangle: "Rectangle") -> str: ...


# --- Елементи --------------------------------------------------------------
class Shape(ABC):
    @abstractmethod
    def accept(self, visitor: Visitor) -> str: ...


class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def accept(self, visitor: Visitor) -> str:
        return visitor.visit_circle(self)


class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        self.width, self.height = width, height

    def accept(self, visitor: Visitor) -> str:
        return visitor.visit_rectangle(self)


# --- Конкретні відвідувачі: нові операції без зміни класів фігур -----------
class AreaVisitor(Visitor):
    def visit_circle(self, circle: Circle) -> str:
        return f"Площа кола: {math.pi * circle.radius ** 2:.2f}"

    def visit_rectangle(self, rectangle: Rectangle) -> str:
        return f"Площа прямокутника: {rectangle.width * rectangle.height:.2f}"


class JsonExportVisitor(Visitor):
    def visit_circle(self, circle: Circle) -> str:
        return f'{{"type": "circle", "radius": {circle.radius}}}'

    def visit_rectangle(self, rectangle: Rectangle) -> str:
        return (f'{{"type": "rectangle", "width": {rectangle.width}, '
                f'"height": {rectangle.height}}}')


if __name__ == "__main__":
    shapes: list[Shape] = [Circle(5), Rectangle(4, 6)]

    for visitor in (AreaVisitor(), JsonExportVisitor()):
        print(f"-- {type(visitor).__name__} --")
        for shape in shapes:
            print(shape.accept(visitor))
