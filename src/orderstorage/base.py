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

    @abstractmethod
    def update_size(self, new_size: int) -> None:
        """Update size."""

    def deregister(self) -> None:
        """Deregister from the tickers."""


class Ticker(ABC):
    @property
    @abstractmethod
    def ticker_id(self) -> str:
        pass

    def register(self, order: Order):
        pass

    def deregister(self, order: Order):
        pass


class OrderStorage(ABC):
    def process_order(self, command: str) -> None:
        pass

    def get_best_bid_and_ask_prices(self, ticker: str) -> Tuple[float, float]:
        pass
