#!/bin/python3

from typing import List


# Complete the 'get_ways' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. LONG_INTEGER_ARRAY c
#
def get_ways(total_amount: int, coins: List[int]) -> int:
    # combinations[amount] = num_combinations
    combinations = {
        0: 1,
    }
    for i in range(1, total_amount + 1):
        combinations[i] = 0

    coins.sort()
    for coin in coins:
        for amount in range(0, total_amount + 1):
            if amount >= coin:
                combinations[amount] += combinations[amount - coin]
    return combinations[total_amount]


def test_get_ways():
    """Test for get_ways function."""
    assert get_ways(total_amount=5, coins=[1, 2, 5]) == 4
    assert get_ways(total_amount=5, coins=[2, 3]) == 1
    assert get_ways(total_amount=3, coins=[8, 3, 1, 2]) == 3
    assert get_ways(total_amount=4, coins=[1, 2, 3]) == 4
    assert get_ways(total_amount=10, coins=[2, 5, 3, 6]) == 5


test_get_ways()
first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
c = list(map(int, input().rstrip().split()))
# Print the number of ways of making change for 'n'
# units using coins having the values given by 'c'
ways = get_ways(total_amount=n, coins=c)
print(ways)
