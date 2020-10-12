#!/bin/python3


def diagonalDifference(arr):
    diagonals = [[], []]
    for i, line in enumerate(arr):
        diagonals[0].append(line[i])
        diagonals[1].append(line[-(i + 1)])
    return abs(sum(diagonals[0]) - sum(diagonals[1]))


def test_diagonalDifference():
    """Test for diagonalDifference function."""
    assert diagonalDifference(arr=[[1, 2, 3], [4, 5, 6], [9, 8, 9]]) == 2
    assert diagonalDifference(arr=[[11, 2, 4], [4, 5, 6], [10, 8, -12]]) == 15


test_diagonalDifference()
n = int(input().strip())
arr = []

for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

result = diagonalDifference(arr)
print(result)
