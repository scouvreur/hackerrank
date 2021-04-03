#!/bin/python3

from typing import List


# Complete the breaking_records function below.
def breaking_records(game_scores: List[int]) -> List[int]:
    num_record_breaks = [
        0,  # for max score
        0,  # for min score
    ]
    min_score = game_scores[0]
    max_score = game_scores[0]
    for score in game_scores:
        if score > max_score:
            num_record_breaks[0] += 1
            # update max score
            max_score = score
        elif score < min_score:
            num_record_breaks[1] += 1
            # update min score
            min_score = score
    return num_record_breaks


def test_breaking_records():
    """Test for breaking_records function."""
    assert breaking_records([12, 24, 10, 24]) == [1, 1]
    assert breaking_records([10, 5, 20, 20, 4, 5, 2, 25, 1]) == [2, 4]
    assert breaking_records([3, 4, 21, 36, 10, 28, 35, 5, 24, 42]) == [4, 0]


test_breaking_records()
n = int(input())
scores = list(map(int, input().rstrip().split()))
result = breaking_records(game_scores=scores)
print(" ".join(map(str, result)))
