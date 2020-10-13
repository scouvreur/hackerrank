#!/bin/python3


def birthday_cake_candles(candles):
    """
    Docs
    """
    tallest = max(candles)
    count = candles.count(tallest)
    return count


def test_birthday_cake_candles():
    """Test for birthday_cake_candles function."""
    assert birthday_cake_candles(candles=[3, 2, 1, 3]) == 2
    assert birthday_cake_candles(candles=[1, 2, 3, 4, 5]) == 1


test_birthday_cake_candles()
candles_count = int(input().strip())
candles = list(map(int, input().rstrip().split()))
result = birthday_cake_candles(candles)
print(result)
