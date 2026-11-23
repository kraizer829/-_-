"""Міст (Bridge) — пульти керування та пристрої."""
from abc import ABC, abstractmethod


# --- Реалізація (одна ієрархія) --------------------------------------------
class Device(ABC):
    @abstractmethod
    def is_enabled(self) -> bool: ...

    @abstractmethod
    def enable(self) -> None: ...

    @abstractmethod
    def disable(self) -> None: ...

    @abstractmethod
    def set_volume(self, level: int) -> None: ...


class TV(Device):
    def __init__(self) -> None:
        self._on, self._volume = False, 10

    def is_enabled(self) -> bool:
        return self._on

    def enable(self) -> None:
        self._on = True
        print("TV увімкнено")

    def disable(self) -> None:
        self._on = False
        print("TV вимкнено")

    def set_volume(self, level: int) -> None:
        self._volume = max(0, min(100, level))
        print(f"TV гучність: {self._volume}")


class Radio(TV):
    def enable(self) -> None:
        self._on = True
        print("Радіо увімкнено")

    def disable(self) -> None:
        self._on = False
        print("Радіо вимкнено")

    def set_volume(self, level: int) -> None:
        self._volume = max(0, min(100, level))
        print(f"Радіо гучність: {self._volume}")


# --- Абстракція (друга ієрархія), тримає міст до реалізації ----------------
class RemoteControl:
    def __init__(self, device: Device) -> None:
        self.device = device

    def toggle_power(self) -> None:
        if self.device.is_enabled():
            self.device.disable()
        else:
            self.device.enable()


class AdvancedRemote(RemoteControl):
    def mute(self) -> None:
        self.device.set_volume(0)


if __name__ == "__main__":
    for device in (TV(), Radio()):
        remote = AdvancedRemote(device)
        remote.toggle_power()
        remote.mute()
        remote.toggle_power()
        print("-" * 25)
