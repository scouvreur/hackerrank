def flipping_matrix(matrix):
    # Write your code here
    dim = len(matrix)
    n = dim // 2

    groups = []
    for j in range(n):
        for i in range(n):
            group = [
                matrix[n + j][n + i],
                matrix[n + j][n - (i + 1)],
                matrix[n - (j + 1)][n + i],
                matrix[n - (j + 1)][n - (i + 1)],
            ]
            groups.append(group)

    max_sum = 0
    for group in groups:
        max_sum += max(group)

    return max_sum


def test_flipping_matrix():
    """Test for flipping_matrix function."""
    # matrixes are 2nx2n
    # n=1, 2x2 example
    matrix_2x2 = [
        [1, 2],
        [3, 4],
    ]
    # return 4
    assert flipping_matrix(matrix_2x2) == 4

    # n=2, 4x4 example
    matrix_4x4_1 = [
        [112, 42, 83, 119],
        [56, 125, 56, 49],
        [15, 78, 101, 43],
        [62, 98, 114, 108],
    ]
    # return 414
    assert flipping_matrix(matrix_4x4_1) == 414

    # n=2, 4x4 example
    matrix_4x4_2 = [
        [107, 54, 128, 15],
        [12, 75, 110, 138],
        [100, 96, 34, 85],
        [75, 15, 28, 112],
    ]
    # return 488
    assert flipping_matrix(matrix_4x4_2) == 488

    # n=3, 6x6 example
    matrix_6x6 = [
        [4089, 1714, 459, 3709, 2113, 773],
        [969, 2435, 2197, 1766, 852, 1278],
        [2235, 1228, 429, 1771, 1832, 3673],
        [2728, 2050, 1747, 3488, 2439, 4086],
        [3451, 3472, 1816, 2635, 1365, 4091],
        [2772, 2673, 3237, 2672, 1182, 2357],
    ]
    # 30682
    assert flipping_matrix(matrix_6x6) == 30682


test_flipping_matrix()
