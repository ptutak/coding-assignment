from abc import ABC, abstractmethod
from typing import Tuple

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

    @property
    @abstractmethod
    def size(self) -> int:
        """Get order size."""

    @abstractmethod
    def update_size(self, new_size: int) -> None:
        """Update size."""

    def deregister(self) -> None:
        """Deregister from the tickers."""


class Ticker(ABC):
    @classmethod
    @abstractmethod
    def get_ticker_by_id(cls, ticker_id: str) -> "Ticker":
        pass

    @property
    @abstractmethod
    def ticker_id(self) -> str:
        pass

    @property
    @abstractmethod
    def best_bid(self) -> float:
        pass

    @property
    @abstractmethod
    def best_ask(self) -> float:
        pass

    def register(self, order: Order):
        pass

    def deregister(self, order: Order):
        pass


class OrderStorage(ABC):
    @abstractmethod
    def process_order(self, command: str) -> None:
        pass

    @abstractmethod
    def get_best_bid_and_ask_prices(self, ticker_id: str) -> Tuple[float, float]:
        pass
