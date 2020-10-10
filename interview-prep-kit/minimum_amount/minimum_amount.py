#!/bin/python3

from typing import List


def calculateAmount(prices: List[int]) -> int:
    """
    This functions takes in the list of prices of the shopper's
    items and returns the total prices after applying the discount.

    Parameters
    ----------
    prices: List[int]
        The list of prices in the

    Returns
    -------
    total: int
        The sum of discounted prices in the items list.
    """
    total = 0
    prior_items_min = 0
    for i in range(len(prices)):
        if i == 0:
            total += prices[i]
            prior_items_min = prices[i]
        else:
            try:
                total += max(prices[i] - prior_items_min, 0)
                prior_items_min = min(prior_items_min, prices[i])
            except IndexError:
                pass
    return total


def test_calculateAmount():
    """Test for calculateAmount function."""
    assert calculateAmount(prices=[2, 5, 1, 4]) == 8
    assert calculateAmount(prices=[4, 9, 2, 3]) == 10
    assert calculateAmount(prices=[1, 2, 3, 4]) == 7


test_calculateAmount()

prices_count = int(input().strip())
prices = []

for _ in range(prices_count):
    prices_item = int(input().strip())
    prices.append(prices_item)

result = calculateAmount(prices)
print(result)
