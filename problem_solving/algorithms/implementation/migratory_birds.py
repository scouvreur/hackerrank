from typing import List


# Complete the migratory_birds function below.
def migratory_birds(array: List[int]) -> int:
    sightings = 6 * [0]
    for bird_id in array:
        sightings[bird_id] += 1
    return sightings.index(max(sightings))


def test_migratory_birds():
    """Test for migratory_birds function."""
    assert migratory_birds(array=[1, 1, 2, 2, 3]) == 1
    assert migratory_birds(array=[1, 4, 4, 4, 5, 3]) == 4
    assert migratory_birds(array=[1, 2, 3, 4, 5, 4, 3, 2, 1, 3, 4]) == 3


test_migratory_birds()
arr_count = int(input().strip())
arr = list(map(int, input().rstrip().split()))
result = migratory_birds(arr)
print(result)
