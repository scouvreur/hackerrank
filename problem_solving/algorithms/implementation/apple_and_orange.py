#!/bin/python3

from typing import List


# Complete the count_apples_and_oranges function below.
def count_apples_and_oranges(
    s: int, t: int, a: int, b: int, apples: List[int], oranges: List[int]
) -> (int, int):
    """ """
    apple_count = 0
    orange_count = 0
    apples_thrown = list(map(lambda x: x + a, apples))
    oranges_thrown = list(map(lambda x: x + b, oranges))
    for apple in apples_thrown:
        if s <= apple <= t:
            apple_count += 1
    for orange in oranges_thrown:
        if s <= orange <= t:
            orange_count += 1
    return (apple_count, orange_count)


def test_count_apples_and_oranges():
    """Test for count_apples_and_oranges function."""
    assert count_apples_and_oranges(
        s=7, t=11, a=5, b=15, apples=[-2, 2, 1], oranges=[5, -6]
    ) == (1, 1)


test_count_apples_and_oranges()
st = input().split()
s = int(st[0])
t = int(st[1])
ab = input().split()
a = int(ab[0])
b = int(ab[1])
mn = input().split()
m = int(mn[0])
n = int(mn[1])
apples = list(map(int, input().rstrip().split()))
oranges = list(map(int, input().rstrip().split()))
result = count_apples_and_oranges(s, t, a, b, apples, oranges)
print(result[0])
print(result[1])
