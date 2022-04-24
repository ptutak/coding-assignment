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
    @property
    @abstractmethod
    def ticker_id(self) -> str:
        """Get ticker id."""

    @property
    @abstractmethod
    def best_bid(self) -> float:
        """Get best bid for ticker."""

    @property
    @abstractmethod
    def best_ask(self) -> float:
        """Get best ask for ticker."""

    def register(self, order: Order):
        """Register an order for ticker."""

    def deregister(self, order: Order):
        """Deregister an order for ticker."""


class OrderStorage(ABC):
    @abstractmethod
    def process_order(self, command: str) -> None:
        """Process order command."""

    @abstractmethod
    def get_best_bid_and_ask_prices(self, ticker_id: str) -> Tuple[float, float]:
        """Get best bid and ask prices for selected ticker."""
