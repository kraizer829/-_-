"""Фасад (Facade) — домашній кінотеатр."""


# --- Складні підсистеми ----------------------------------------------------
class Lights:
    def dim(self) -> None:
        print("Світло приглушено")

    def on(self) -> None:
        print("Світло увімкнено")


class Projector:
    def on(self) -> None:
        print("Проєктор увімкнено")

    def off(self) -> None:
        print("Проєктор вимкнено")


class SoundSystem:
    def on(self) -> None:
        print("Звукову систему увімкнено")

    def set_surround(self) -> None:
        print("Режим об'ємного звуку")

    def off(self) -> None:
        print("Звукову систему вимкнено")


class Player:
    def play(self, movie: str) -> None:
        print(f"Відтворення фільму «{movie}»")

    def stop(self) -> None:
        print("Відтворення зупинено")


# --- Фасад -----------------------------------------------------------------
class HomeTheaterFacade:
    def __init__(self) -> None:
        self.lights = Lights()
        self.projector = Projector()
        self.sound = SoundSystem()
        self.player = Player()

    def watch_movie(self, movie: str) -> None:
        print("== Готуємося до перегляду ==")
        self.lights.dim()
        self.projector.on()
        self.sound.on()
        self.sound.set_surround()
        self.player.play(movie)

    def end_movie(self) -> None:
        print("== Завершуємо перегляд ==")
        self.player.stop()
        self.sound.off()
        self.projector.off()
        self.lights.on()


if __name__ == "__main__":
    theater = HomeTheaterFacade()
    theater.watch_movie("Матриця")
    theater.end_movie()
