#!/bin/python3


def plus_minus(array):
    ratio_positive = round(sum(i > 0 for i in array) / len(array), 6)
    ratio_negative = round(sum(i < 0 for i in array) / len(array), 6)
    ratio_zero = round(sum(i == 0 for i in array) / len(array), 6)
    return ratio_positive, ratio_negative, ratio_zero


def test_plus_minus():
    """Test for plus_minus function."""
    assert plus_minus(array=[1, 1, 0, -1, -1]) == (
        0.400000,
        0.400000,
        0.200000,
    )
    assert plus_minus(array=[-4, 3, -9, 0, 4, 1]) == (
        0.500000,
        0.333333,
        0.166667,
    )


test_plus_minus()
n = int(input())
array = list(map(int, input().rstrip().split()))
for ratio in plus_minus(array):
    print(ratio)
