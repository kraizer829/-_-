"""Одинак (Singleton) — глобальна конфігурація застосунку."""
import threading


class AppConfig:
    _instance: "AppConfig | None" = None
    _lock = threading.Lock()

    def __new__(cls) -> "AppConfig":
        # Подвійна перевірка: безпечно для багатопоточності
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    instance = super().__new__(cls)
                    instance.settings = {"language": "uk", "debug": False}
                    cls._instance = instance
        return cls._instance

    def set(self, key: str, value) -> None:
        self.settings[key] = value

    def get(self, key: str):
        return self.settings.get(key)


if __name__ == "__main__":
    a = AppConfig()
    b = AppConfig()

    a.set("debug", True)

    print("a is b:", a is b)
    print("b.debug =", b.get("debug"))  # True, бо це той самий об'єкт
