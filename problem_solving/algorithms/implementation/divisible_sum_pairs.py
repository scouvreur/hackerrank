from typing import List


# Complete the divisible_sum_pairs function below.
def divisible_sum_pairs(k: int, array: List[int]) -> int:
    pairs = []
    for i in range(len(array)):
        subarray = array[i:]
        if len(subarray) >= 2:
            first = subarray[0]
            for num in subarray[1:]:
                if (first + num) % k == 0:
                    pairs.append([first, num])
    return len(pairs)


def test_divisible_sum_pairs():
    """Test for divisible_sum_pairs function."""
    assert divisible_sum_pairs(k=5, array=[1, 2, 3, 4, 5, 6]) == 3
    assert divisible_sum_pairs(k=3, array=[1, 3, 2, 6, 1, 2]) == 5


test_divisible_sum_pairs()
nk = input().split()
k = int(nk[1])
ar = list(map(int, input().rstrip().split()))
result = divisible_sum_pairs(k, ar)
print(result)
