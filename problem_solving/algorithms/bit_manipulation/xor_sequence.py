#!/bin/python3

A = {0: 0}


def get_xor_sequence(l, r):
    global A
    if r >= len(A):
        starting_index = min(l, len(A))
        for i in range(starting_index, r + 1):
            A[i] = A[i - 1] ^ i
    return list(A.values())[l : r + 1]


# Complete the xor_sequence function below.
def xor_sequence(l, r):
    sequence = get_xor_sequence(l, r)
    xor = 0
    for item in sequence:
        xor = xor ^ item
    return xor


def test_get_xor_sequence():
    """Test for get_xor_sequence function."""
    assert get_xor_sequence(l=0, r=0) == [0]
    assert get_xor_sequence(l=1, r=4) == [1, 3, 0, 4]
    assert get_xor_sequence(l=2, r=4) == [3, 0, 4]
    assert get_xor_sequence(l=2, r=8) == [3, 0, 4, 1, 7, 0, 8]
    assert get_xor_sequence(l=5, r=9) == [1, 7, 0, 8, 1]
    assert get_xor_sequence(l=3, r=5) == [0, 4, 1]
    assert get_xor_sequence(l=4, r=6) == [4, 1, 7]
    assert get_xor_sequence(l=15, r=20) == [0, 16, 1, 19, 0, 20]


def test_xor_sequence():
    """Test for the xor_sequence function."""
    assert xor_sequence(l=0, r=0) == 0
    assert xor_sequence(l=1, r=4) == 6
    assert xor_sequence(l=2, r=4) == 7
    assert xor_sequence(l=2, r=8) == 9
    assert xor_sequence(l=5, r=9) == 15
    assert xor_sequence(l=3, r=5) == 5
    assert xor_sequence(l=4, r=6) == 2
    assert xor_sequence(l=15, r=20) == 22


test_get_xor_sequence()
test_xor_sequence()
q = int(input())
for _ in range(q):
    lr = input().split()
    l = int(lr[0])
    r = int(lr[1])
    result = xor_sequence(l, r)
    print(result)
