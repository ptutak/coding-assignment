from typing import Dict, Tuple

from orderstorage.exceptions import OrderAlreadyPresentException, OrderNotFoundException

from .base import OrderStorage
from .order import MemoryOrder
from .ticker import MemoryTicker


class MemoryOrderStorage(OrderStorage):
    def __init__(self) -> None:
        self._orders: Dict[str, MemoryOrder] = {}

    def process_order(self, command: str) -> None:
        splitted_command = command.split("|")
        order_id = splitted_command[1]
        command_type = splitted_command[2]
        if command_type == "a":
            if order_id in self._orders:
                raise OrderAlreadyPresentException(f"Order with id {order_id} is already present.")
            ticker_id = splitted_command[3]
            ticker = MemoryTicker.get_ticker_by_id(ticker_id)
            side = splitted_command[4]
            price = float(splitted_command[5])
            size = int(splitted_command[6])
            order = MemoryOrder(order_id, side, price, size, ticker)
            self._orders[order_id] = order

        elif command_type == "u":
            if order_id not in self._orders:
                raise OrderNotFoundException(f"Order with id {order_id} was not found.")
            updated_size = int(splitted_command[3])
            self._orders[order_id].update_size(updated_size)

        else:
            if order_id not in self._orders:
                raise OrderNotFoundException(f"Order with id {order_id} was not found.")
            self._orders[order_id].deregister()
            del self._orders[order_id]

    def get_best_bid_and_ask_prices(self, ticker_id: str) -> Tuple[float, float]:
        ticker = MemoryTicker.get_ticker_by_id(ticker_id)
        return (ticker.best_bid, ticker.best_ask)
