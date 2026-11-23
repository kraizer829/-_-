"""Будівельник (Builder) — збирання комп'ютера крок за кроком."""
from dataclasses import dataclass


# --- Продукт ---------------------------------------------------------------
@dataclass
class Computer:
    cpu: str = ""
    ram: int = 0
    storage: str = ""
    gpu: str | None = None

    def __str__(self) -> str:
        gpu = self.gpu or "вбудована"
        return (f"CPU: {self.cpu}, RAM: {self.ram} ГБ, "
                f"накопичувач: {self.storage}, GPU: {gpu}")


# --- Будівельник -----------------------------------------------------------
class ComputerBuilder:
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> "ComputerBuilder":
        self._computer = Computer()
        return self

    def set_cpu(self, cpu: str) -> "ComputerBuilder":
        self._computer.cpu = cpu
        return self

    def set_ram(self, gb: int) -> "ComputerBuilder":
        self._computer.ram = gb
        return self

    def set_storage(self, storage: str) -> "ComputerBuilder":
        self._computer.storage = storage
        return self

    def set_gpu(self, gpu: str) -> "ComputerBuilder":
        self._computer.gpu = gpu
        return self

    def build(self) -> Computer:
        result = self._computer
        self.reset()
        return result


# --- Директор: знає готові «рецепти» ---------------------------------------
class Director:
    def __init__(self, builder: ComputerBuilder) -> None:
        self.builder = builder

    def office_pc(self) -> Computer:
        return (self.builder.set_cpu("Intel Core i3").set_ram(8)
                .set_storage("SSD 256 ГБ").build())

    def gaming_pc(self) -> Computer:
        return (self.builder.set_cpu("AMD Ryzen 9").set_ram(32)
                .set_storage("SSD 2 ТБ").set_gpu("RTX 4080").build())


if __name__ == "__main__":
    director = Director(ComputerBuilder())
    print("Офісний:", director.office_pc())
    print("Ігровий:", director.gaming_pc())

    # Можна будувати й напряму, без директора
    custom = (ComputerBuilder().set_cpu("Apple M3").set_ram(16)
              .set_storage("SSD 512 ГБ").build())
    print("Власний:", custom)
