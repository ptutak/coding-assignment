from typing import Tuple

from .base import OrderStorage
from .orderstorage import MemoryOrderStorage

__all__ = ["getOrderBook", "processOrder", "getBestBidAndAsk"]


def getOrderBook() -> MemoryOrderStorage:
    return MemoryOrderStorage()


def processOrder(orderbook: OrderStorage, order: str) -> None:
    orderbook.process_order(order)


def getBestBidAndAsk(orderbook: OrderStorage, ticker: str) -> Tuple[float, float]:
    return orderbook.get_best_bid_and_ask_prices(ticker)
