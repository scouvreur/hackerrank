#!/bin/python3


# Complete the maximizing_xor function below.
def maximizing_xor(left, right):
    max_xor = 0
    for i in range(left, right + 1):
        for j in range(left, right + 1):
            xor = i ^ j
            if xor > max_xor:
                max_xor = xor
    return max_xor


def test_maximizing_xor():
    """Test for maximizing_xor function."""
    assert maximizing_xor(left=11, right=12) == 7
    assert maximizing_xor(left=10, right=15) == 7
    assert maximizing_xor(left=11, right=100) == 127
    assert maximizing_xor(left=5, right=6) == 3
    assert maximizing_xor(left=1, right=1000) == 1023
    assert maximizing_xor(left=304, right=313) == 15
    assert maximizing_xor(left=578, right=909) == 511


test_maximizing_xor()
left = int(input())
right = int(input())
result = maximizing_xor(left, right)
print(result)
