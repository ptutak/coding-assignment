from orderstorage.const import Side
from orderstorage.order import MemoryOrder
from orderstorage.ticker import MemoryTicker


def test_order(clear_classes):
    ticker = MemoryTicker.get_ticker_by_id("AAA")
    order = MemoryOrder("aabbb", "S", 120.0, 54, ticker)

    assert order.order_id == "aabbb"
    assert order.price == 120.0
    assert order.side == Side.ASK
    assert order.size == 54

    order.update_size(33)
    assert order.size == 33


def test_order_with_ticker(clear_classes):
    ticker = MemoryTicker.get_ticker_by_id("AAA")
    MemoryOrder("aabbb", "S", 120.0, 54, ticker)

    assert ticker.best_ask == 120.0
    assert ticker.best_bid == 0.0

    order_2 = MemoryOrder("ccbbb", "S", 125.0, 40, ticker)

    assert ticker.best_ask == 125.0

    order_2.deregister()

    assert ticker.best_ask == 120.0
