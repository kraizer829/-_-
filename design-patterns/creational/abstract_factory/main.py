"""Абстрактна фабрика (Abstract Factory) — елементи інтерфейсу для різних ОС."""
from abc import ABC, abstractmethod


# --- Абстрактні продукти ---------------------------------------------------
class Button(ABC):
    @abstractmethod
    def render(self) -> str: ...


class Checkbox(ABC):
    @abstractmethod
    def render(self) -> str: ...


# --- Конкретні продукти: Windows ------------------------------------------
class WindowsButton(Button):
    def render(self) -> str:
        return "[Windows] кнопка з прямими кутами"


class WindowsCheckbox(Checkbox):
    def render(self) -> str:
        return "[Windows] квадратний чекбокс"


# --- Конкретні продукти: macOS --------------------------------------------
class MacButton(Button):
    def render(self) -> str:
        return "[macOS] кругла кнопка із тінню"


class MacCheckbox(Checkbox):
    def render(self) -> str:
        return "[macOS] заокруглений чекбокс"


# --- Абстрактна фабрика ----------------------------------------------------
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button: ...

    @abstractmethod
    def create_checkbox(self) -> Checkbox: ...


class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()


class MacFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()


# --- Клієнтський код -------------------------------------------------------
def build_form(factory: GUIFactory) -> None:
    print(factory.create_button().render())
    print(factory.create_checkbox().render())


if __name__ == "__main__":
    for factory in (WindowsFactory(), MacFactory()):
        build_form(factory)
        print("-" * 30)
