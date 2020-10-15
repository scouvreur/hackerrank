#!/bin/python3


# Complete the lonelyinteger function below.
def lonely_integer(array):
    counts = {}
    for item in array:
        try:
            counts[item] += 1
        except KeyError:
            counts[item] = 1
    return min(counts, key=counts.get)


def test_lone_integer():
    """Test for lonely_integer function."""
    assert lonely_integer(array=[1]) == 1
    assert lonely_integer(array=[1, 1, 2]) == 2
    assert lonely_integer(array=[1, 2, 3, 4, 3, 2, 1]) == 4
    assert lonely_integer(array=[0, 0, 1, 2, 1]) == 2


n = int(input())
a = list(map(int, input().rstrip().split()))
result = lonely_integer(array=a)
print(result)
