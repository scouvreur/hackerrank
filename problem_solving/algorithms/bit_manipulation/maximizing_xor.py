#!/bin/python3


# Complete the maximizing_xor function below.
def maximizing_xor(l, r):
    max_xor = 0
    for i in range(l, r + 1):
        for j in range(l, r + 1):
            xor = i ^ j
            if xor > max_xor:
                max_xor = xor
    return max_xor


def test_maximizing_xor():
    """Test for maximizing_xor function."""
    assert maximizing_xor(l=11, r=12) == 7
    assert maximizing_xor(l=10, r=15) == 7
    assert maximizing_xor(l=11, r=100) == 127
    assert maximizing_xor(l=5, r=6) == 3
    assert maximizing_xor(l=1, r=1000) == 1023
    assert maximizing_xor(l=304, r=313) == 15
    assert maximizing_xor(l=578, r=909) == 511


test_maximizing_xor()
l = int(input())
r = int(input())
result = maximizing_xor(l, r)
print(result)
