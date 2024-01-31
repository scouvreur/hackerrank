def hourglass_sum(array):
    # there are 16 hourglasses
    hourglasses = []
    for row in range(4):
        for col in range(4):
            hourglasses.append(
                sum(array[row][col : col + 3])
                + array[row + 1][col + 1]
                + sum(array[row + 2][col : col + 3])
            )

    return max(hourglasses)


def test_hourglass_sum():
    """Test for hourglass_sum function."""
    array = [
        [-9, -9, -9, 1, 1, 1],
        [0, -9, 0, 4, 3, 2],
        [-9, -9, -9, 1, 2, 3],
        [0, 0, 8, 6, 6, 0],
        [0, 0, 0, -2, 0, 0],
        [0, 0, 1, 2, 4, 0],
    ]
    assert hourglass_sum(array) == 28


test_hourglass_sum()
