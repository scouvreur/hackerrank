#!/bin/python3

import pytest


def tranform_cost(array_1, array_2):
    cost = 0
    for a, b in zip(array_1, array_2):
        for i in range(len(array_1)):
            if a[i] != b[i]:
                cost += abs(b[i] - a[i])
    return cost


def get_row_col_diag_sums(array):
    columns = [[], [], []]
    for i in range(len(array)):
        for row in array:
            columns[i].append(row[i])
    diagonals = [[], []]
    for i, row in enumerate(array):
        diagonals[0].append(row[i])
        diagonals[1].append(row[-(i + 1)])
    row_sums = [sum(row) for row in array]
    column_sums = [sum(column) for column in columns]
    diagonal_sums = [sum(diagonal) for diagonal in diagonals]
    return row_sums, column_sums, diagonal_sums


def is_magic(array):
    """
    Given array, returns whether it is magic. An array is magic if the sum
    of any row, column, or diagonal of length  is always equal to the same
    number: the magic constant.
    """
    row_sums, column_sums, diagonal_sums = get_row_col_diag_sums(array)
    return (
        all(sum == column_sums[0] for sum in column_sums)
        and all(sum == diagonal_sums[0] for sum in diagonal_sums)
        and all(sum == row_sums[0] for sum in row_sums)
        and column_sums[0] == diagonal_sums[0]
        and diagonal_sums[0] == row_sums[0]
    )


def formingMagicSquare(s):
    pass


def test_tranform_cost():
    """Test for tranform_cost function."""
    assert (
        tranform_cost(
            array_1=[[5, 3, 4], [1, 5, 8], [6, 4, 2]],
            array_2=[[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        )
        == 7
    )


def test_get_row_col_diag_sums():
    """Test for get_row_diag_sums function."""
    array = [[8, 3, 4], [1, 5, 9], [6, 7, 2]]
    row_sums, column_sums, diagonal_sums = get_row_col_diag_sums(array)
    assert row_sums == [15, 15, 15]
    assert column_sums == [15, 15, 15]
    assert diagonal_sums == [15, 15]


def test_is_magic():
    """Test for is_magic function."""
    assert is_magic(array=[[5, 3, 4], [1, 5, 8], [6, 4, 2]]) is False
    assert is_magic(array=[[8, 3, 4], [1, 5, 9], [6, 7, 2]]) is True


@pytest.mark.skip
def test_formingMagicSquare():
    """Test for formingMagicSquare function."""
    assert formingMagicSquare(s=[[4, 9, 2], [3, 5, 7], [8, 1, 5]]) == 1
    assert formingMagicSquare(s=[[4, 8, 2], [4, 5, 7], [6, 1, 6]]) == 4


def execute_test_cases():
    s = []
    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)
    print(result)


# execute_test_cases()
