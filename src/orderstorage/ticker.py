from typing import List

from .base import Order, Ticker


class MemoryTicker(Ticker):
    def __init__(self) -> None:
        self._bid_side: List[Order] = []
        self._ask_side: List[Order] = []

    def register(self, order: Order):
        order.side
        order.ticker_register(self)
