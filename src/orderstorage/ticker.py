from bisect import insort_left
from typing import List, Set

from .base import Order, Ticker
from .const import Side


class MemoryTicker(Ticker):
    def __init__(self, ticker_id: str) -> None:
        self._ask_side: List[Order] = []
        self._ask_orders: Set[str] = set()
        self._bid_side: List[Order] = []
        self._ticker_id = ticker_id

    @property
    def ticker_id(self) -> str:
        return self._ticker_id

    @property
    def best_ask(self) -> float:
        if self._ask_side:
            return self._ask_side[-1].price
        return 0.0

    @property
    def best_bid(self) -> float:
        if self._bid_side:
            return self._bid_side[-1].price
        return 0.0

    def register(self, order: Order) -> None:
        if order.side == Side.ASK:
            insort_left(self._ask_side, order, key=lambda x: x.price)
            self._ask_orders.add(order.order_id)
        else:
            insort_left(self._bid_side, order, key=lambda x: x.price)

    def deregister(self, order: Order) -> None:
        if order.order_id in self._ask_orders:
            self._ask_side.remove(order)
            self._ask_orders.remove(order.order_id)
        else:
            self._bid_side.remove(order)
