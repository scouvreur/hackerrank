#!/bin/python3


def mini_max_sum(array):
    """
    Docs
    """
    array.sort()
    min_sum = sum(array[:-1])
    max_sum = sum(array[1:])
    return min_sum, max_sum


def test_mini_max_sum():
    """Test for mini_max_sum function."""
    assert mini_max_sum(array=[1, 3, 5, 7, 9]) == (16, 24)
    assert mini_max_sum(array=[1, 2, 3, 4, 5]) == (10, 14)


test_mini_max_sum()
arr = list(map(int, input().rstrip().split()))
min_sum, max_sum = mini_max_sum(arr)
print(min_sum, max_sum)
