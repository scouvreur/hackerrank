#!/bin/python3

from typing import List

a = list(map(int, input().rstrip().split()))
b = list(map(int, input().rstrip().split()))


# Complete the compareTriplets function below.
def compareTriplets(a: List[int], b: List[int]) -> List[int]:
    score_a, score_b = 0, 0
    assert len(a) == 3, "a is not a triplet"
    assert len(b) == 3, "b is not a triplet"
    for i in range(3):
        if a[i] > b[i]:
            score_a += 1
        elif a[i] < b[i]:
            score_b += 1
    return [score_a, score_b]


result = compareTriplets(a, b)
print(" ".join(map(str, result)))
