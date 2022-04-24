from orderstorage.const import Side
from .base import Order, Ticker


class MemoryOrder(Order):
    def __init__(self, order_id: str, side: str, price: float, size: int, ticker: Ticker) -> None:
        self._id = order_id
        self._price = price
        self._size = size
        self._side = Side(side)
        self._ticker = ticker
        self._ticker.register(self)

    @property
    def order_id(self) -> str:
        return self._id

    @property
    def side(self) -> Side:
        return self._side

    @property
    def price(self) -> float:
        return self._price

    def update_size(self, new_size: int) -> None:
        self._size = new_size

    def deregister(self) -> None:
        self._ticker.deregister(self)
