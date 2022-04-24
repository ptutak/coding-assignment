from orderstorage import getBestBidAndAsk, getOrderBook, processOrder


def test_access_functions():
    orderbook = getOrderBook()
    assert getBestBidAndAsk(orderbook, "AAA") == (0, 0)

    processOrder(orderbook, "1234|abbb11|a|AAA|B|205.00000|100")
    assert getBestBidAndAsk(orderbook, "AAA") == (205.0, 0)

    processOrder(orderbook, "1235|abbb11|u|55")
    assert getBestBidAndAsk(orderbook, "AAA") == (205.0, 0)

    processOrder(orderbook, "1236|abbb13|a|AAA|B|207.00000|24")
    processOrder(orderbook, "1237|abcb11|a|AAA|S|100.00000|125")

    assert getBestBidAndAsk(orderbook, "AAA") == (207.0, 100.0)

    processOrder(orderbook, "1238|abbb12|a|AAA|B|206.00000|27")
    processOrder(orderbook, "1239|abbb11|c")

    assert getBestBidAndAsk(orderbook, "AAA") == (207.0, 100.0)

    processOrder(orderbook, "1240|abbb13|c")

    assert getBestBidAndAsk(orderbook, "AAA") == (206.0, 100.0)

    processOrder(orderbook, "1241|abbb12|c")

    assert getBestBidAndAsk(orderbook, "AAA") == (0.0, 100.0)
