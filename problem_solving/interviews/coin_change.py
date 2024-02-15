from typing import List


def min_coins(coins: List[int], target: int) -> int:
    # initialize values
    min_num_coins = 0
    remainder = target

    # sort coins in descending order
    coins.sort(reverse=True)  # O(n log n)

    # O(number of possible coins)
    for coin in coins:
        if coin <= remainder:
            num_coins = int(remainder / coin)
            min_num_coins += num_coins
            remainder -= coin * num_coins

    # handle cases when no change can be provided
    if remainder > 0:
        return -1
    else:
        return min_num_coins


coins = [2, 5, 20, 50, 100, 200]
target = 60

target = 600
target = 665


def test_min_coins():
    """Test for min_coins function."""
    coins = [10, 20, 50, 100, 200]
    assert (min_coins(coins, target=660)) == 5  # 200 + 200 + 200 + 50 + 10
    assert (min_coins(coins, target=300)) == 2  # 200 + 100


test_min_coins()

print(min_coins(coins, target=225))
