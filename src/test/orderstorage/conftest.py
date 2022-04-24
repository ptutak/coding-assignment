from pytest import fixture

from orderstorage.ticker import MemoryTicker


@fixture
def clear_classes():
    MemoryTicker._instances = {}
