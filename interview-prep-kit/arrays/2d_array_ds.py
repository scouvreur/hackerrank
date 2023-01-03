#!/bin/python3

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#
def hourglass_sum(array):
    """

    """
    return None


def test_hourglass_sum():
    assert hourglass_sum(array=test_1) == 5
    assert hourglass_sum(array=test_2) == 19
    assert hourglass_sum(array=test_3) == 15


def get_hourglasses(array):
    return None


if __name__ == "__main__":
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    result = hourglass_sum(arr)
    print(result)


test_1 = [
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
]

test_2 = [
    [-9, -9, -9, 1, 1, 1],
    [0, -9, 0, 4, 3, 2],
    [-9, -9, -9, 1, 2, 3],
    [0, 0, 8, 6, 6, 0],
    [0, 0, 0, -2, 0, 0],
    [0, 0, 1, 2, 4, 0],
]

test_2_hourglass_sum = [
    -63,
    -34,
    -9,
    12,
    -10,
    0,
    28,
    23,
    -27,
    -11,
    -2,
    10,
    9,
    17,
    25,
    18,
]

test_3 = [
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0],
]
