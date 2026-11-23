"""Адаптер (Adapter) — підключення стороннього платіжного сервісу."""


# --- Цільовий інтерфейс, який очікує наш застосунок ------------------------
class PaymentProcessor:
    def pay(self, amount_uah: float) -> str:
        raise NotImplementedError


class OurPayment(PaymentProcessor):
    def pay(self, amount_uah: float) -> str:
        return f"Оплата {amount_uah:.2f} грн через наш сервіс"


# --- Сторонній клас із несумісним інтерфейсом ------------------------------
class ForeignGateway:
    def make_transaction(self, cents: int, currency: str) -> str:
        return f"Foreign gateway: {cents / 100:.2f} {currency}"


# --- Адаптер ---------------------------------------------------------------
class ForeignGatewayAdapter(PaymentProcessor):
    def __init__(self, gateway: ForeignGateway) -> None:
        self._gateway = gateway

    def pay(self, amount_uah: float) -> str:
        cents = int(round(amount_uah * 100))
        return self._gateway.make_transaction(cents, "UAH")


def checkout(processor: PaymentProcessor, amount: float) -> None:
    print(processor.pay(amount))


if __name__ == "__main__":
    checkout(OurPayment(), 199.5)
    checkout(ForeignGatewayAdapter(ForeignGateway()), 199.5)
