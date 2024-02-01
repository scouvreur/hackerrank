from typing import List


def dynamic_array(n: int, queries: List[List[int]]) -> List[int]:
    # Write your code here
    array = [[] for _ in range(n)]
    last_answer = 0
    answers = []

    for query in queries:
        query_type = query[0]
        x = query[1]
        y = query[2]

        index = (x ^ last_answer) % n

        if query_type == 1:
            array[index].append(y)
        elif query_type == 2:
            last_answer = array[index][y % len(array[index])]
            answers.append(last_answer)

    return answers


def test_dynamic_array():
    """Test for dynamic_array function."""
    n = 2

    queries = [
        [1, 0, 5],
        [1, 1, 7],
        [1, 0, 3],
        [2, 1, 0],
        [2, 1, 1],
    ]
    assert dynamic_array(n, queries) == [7, 3]


test_dynamic_array()
