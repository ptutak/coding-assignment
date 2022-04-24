from typing import Dict, List, Set

from .base import Order, Ticker
from .const import Side
from bisect import insort_left


class MemoryTicker(Ticker):
    def __init__(self) -> None:
        self._ask_side: List[Order] = []
        self._ask_orders: Set[str] = set()
        self._bid_side: List[Order] = []

    def register(self, order: Order):
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
