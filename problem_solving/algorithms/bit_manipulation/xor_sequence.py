#!/bin/python3

A = {0: 0}


def get_xor_sequence(left, right):
    global A
    if right >= len(A):
        starting_index = min(left, len(A))
        for i in range(starting_index, right + 1):
            A[i] = A[i - 1] ^ i
    return list(A.values())[left : right + 1]


# Complete the xor_sequence function below.
def xor_sequence(left, right):
    sequence = get_xor_sequence(left, right)
    xor = 0
    for item in sequence:
        xor = xor ^ item
    return xor


def test_get_xor_sequence():
    """Test for get_xor_sequence function."""
    assert get_xor_sequence(left=0, right=0) == [0]
    assert get_xor_sequence(left=1, right=4) == [1, 3, 0, 4]
    assert get_xor_sequence(left=2, right=4) == [3, 0, 4]
    assert get_xor_sequence(left=2, right=8) == [3, 0, 4, 1, 7, 0, 8]
    assert get_xor_sequence(left=5, right=9) == [1, 7, 0, 8, 1]
    assert get_xor_sequence(left=3, right=5) == [0, 4, 1]
    assert get_xor_sequence(left=4, right=6) == [4, 1, 7]
    assert get_xor_sequence(left=15, right=20) == [0, 16, 1, 19, 0, 20]


def test_xor_sequence():
    """Test for the xor_sequence function."""
    assert xor_sequence(left=0, right=0) == 0
    assert xor_sequence(left=1, right=4) == 6
    assert xor_sequence(left=2, right=4) == 7
    assert xor_sequence(left=2, right=8) == 9
    assert xor_sequence(left=5, right=9) == 15
    assert xor_sequence(left=3, right=5) == 5
    assert xor_sequence(left=4, right=6) == 2
    assert xor_sequence(left=15, right=20) == 22


test_get_xor_sequence()
test_xor_sequence()
q = int(input())
for _ in range(q):
    left_right = input().split()
    left = int(left_right[0])
    right = int(left_right[1])
    result = xor_sequence(left, right)
    print(result)
