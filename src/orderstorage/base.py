from abc import ABC, abstractmethod

from .const import Side


class Order(ABC):
    @property
    @abstractmethod
    def order_id(self) -> str:
        """Order id."""

    @property
    @abstractmethod
    def side(self) -> Side:
        """Return the side."""

    @property
    @abstractmethod
    def price(self) -> float:
        """Return the order price"""

    @abstractmethod
    def update_size(self, new_size: int) -> None:
        """Update size."""

    def ticker_register(self, ticker: "Ticker"):
        "Register the ticker."

    def deregister(self) -> None:
        """Deregister from the tickers."""


class Ticker(ABC):
    def register(self, order: Order):
        pass

    def deregister(self, order: Order):
        pass


class OrderStorage(ABC):
    pass
