#!/bin/python3

from typing import List


# Complete the equal function below.
def equal(colleagues: List[int]) -> int:
    rounds = 0
    chocolates = [1, 2, 5]
    min_chocolates = min(colleagues)
    colleagues = list(map(lambda x: x - min_chocolates, colleagues))
    for chocolate in chocolates:
        pass
    return rounds


def test_equal():
    """Test for equal function."""
    assert equal(colleagues=[1, 1, 5]) == 2
    assert equal(colleagues=[2, 2, 3, 7]) == 2
    assert equal(colleagues=[10, 7, 12]) == 3


test_equal()
# t = int(input())
# for t_itr in range(t):
#     n = int(input())
#     arr = list(map(int, input().rstrip().split()))
#     result = equal(arr)
#     print(result)
