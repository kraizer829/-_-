"""Замісник (Proxy) — ледаче завантаження зображення з кешуванням і контролем доступу."""
from abc import ABC, abstractmethod


class Image(ABC):
    @abstractmethod
    def display(self) -> str: ...


class RealImage(Image):
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self._load()

    def _load(self) -> None:
        print(f"[RealImage] Завантаження великого файлу {self.filename}...")

    def display(self) -> str:
        return f"Показ зображення {self.filename}"


class ImageProxy(Image):
    def __init__(self, filename: str, user_role: str) -> None:
        self.filename = filename
        self.user_role = user_role
        self._real: RealImage | None = None

    def display(self) -> str:
        # Захисний замісник: перевірка прав доступу
        if self.user_role != "admin":
            return "Доступ заборонено"
        # Віртуальний замісник: створюємо реальний об'єкт лише за потреби
        if self._real is None:
            self._real = RealImage(self.filename)
        return self._real.display()


if __name__ == "__main__":
    guest = ImageProxy("photo.png", "guest")
    print(guest.display())

    admin = ImageProxy("photo.png", "admin")
    print("Проксі створено, файл ще не завантажено.")
    print(admin.display())   # завантаження відбувається тут
    print(admin.display())   # вдруге — без повторного завантаження
