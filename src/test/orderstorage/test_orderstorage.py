import pytest

from orderstorage.exceptions import OrderAlreadyPresentException, OrderNotFoundException
from orderstorage.orderstorage import MemoryOrderStorage


def test_memory_orderstorage(clear_classes):
    memory_order_storage = MemoryOrderStorage()

    assert memory_order_storage.get_best_bid_and_ask_prices("AAA") == (0, 0)

    memory_order_storage.process_order("1234|abbb11|a|AAA|B|205.00000|100")

    assert memory_order_storage.get_best_bid_and_ask_prices("AAA") == (205.0, 0)

    memory_order_storage.process_order("1235|abbb11|u|55")

    assert memory_order_storage.get_best_bid_and_ask_prices("AAA") == (205.0, 0)

    with pytest.raises(OrderAlreadyPresentException):
        memory_order_storage.process_order("1234|abbb11|a|AAA|B|200.00000|110")

    with pytest.raises(OrderNotFoundException):
        memory_order_storage.process_order("1235|abbb12|u|55")

    memory_order_storage.process_order("1236|abbb13|a|AAA|B|207.00000|24")
    memory_order_storage.process_order("1237|abcb11|a|AAA|S|100.00000|125")

    assert memory_order_storage.get_best_bid_and_ask_prices("AAA") == (207.0, 100.0)

    memory_order_storage.process_order("1238|abbb12|a|AAA|B|206.00000|27")
    memory_order_storage.process_order("1239|abbb11|c")

    assert memory_order_storage.get_best_bid_and_ask_prices("AAA") == (207.0, 100.0)

    memory_order_storage.process_order("1240|abbb13|c")

    assert memory_order_storage.get_best_bid_and_ask_prices("AAA") == (206.0, 100.0)

    memory_order_storage.process_order("1241|abbb12|c")

    assert memory_order_storage.get_best_bid_and_ask_prices("AAA") == (0.0, 100.0)
