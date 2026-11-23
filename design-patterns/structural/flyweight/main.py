"""Легковаговик (Flyweight) — ліс із великою кількістю дерев."""
import sys
from dataclasses import dataclass


# --- Легковаговик: спільний (внутрішній) стан ------------------------------
@dataclass(frozen=True)
class TreeType:
    name: str
    color: str
    texture: str  # умовно «важкі» дані


class TreeFactory:
    _types: dict[tuple, TreeType] = {}

    @classmethod
    def get_tree_type(cls, name: str, color: str, texture: str) -> TreeType:
        key = (name, color, texture)
        if key not in cls._types:
            cls._types[key] = TreeType(name, color, texture)
        return cls._types[key]

    @classmethod
    def count(cls) -> int:
        return len(cls._types)


# --- Контекст: унікальний (зовнішній) стан ---------------------------------
class Tree:
    def __init__(self, x: int, y: int, tree_type: TreeType) -> None:
        self.x, self.y, self.type = x, y, tree_type

    def draw(self) -> str:
        return f"{self.type.name} ({self.type.color}) у точці ({self.x}, {self.y})"


class Forest:
    def __init__(self) -> None:
        self.trees: list[Tree] = []

    def plant(self, x: int, y: int, name: str, color: str, texture: str) -> None:
        tree_type = TreeFactory.get_tree_type(name, color, texture)
        self.trees.append(Tree(x, y, tree_type))


if __name__ == "__main__":
    forest = Forest()
    for i in range(1000):
        forest.plant(i, i * 2, "Дуб", "зелений", "oak.png")
        forest.plant(i, i * 3, "Береза", "білий", "birch.png")

    print("Дерев у лісі:", len(forest.trees))
    print("Різних типів (об'єктів-легковаговиків):", TreeFactory.count())
    print("Приклад:", forest.trees[0].draw())
    print("Один спільний тип використовують усі однакові дерева:",
          forest.trees[0].type is forest.trees[2].type)
