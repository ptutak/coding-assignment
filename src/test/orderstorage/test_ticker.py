from orderstorage.ticker import MemoryTicker


def test_ticker(clear_classes):
    ticker = MemoryTicker.get_ticker_by_id("AAA")
    assert ticker.ticker_id == "AAA"
    assert ticker.best_bid == 0.0
    assert ticker.best_ask == 0.0
