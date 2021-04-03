from typing import List


# Complete the birthday function below.
def birthday(s: List[int], d: int, m: int) -> int:
    n_segments = 0
    for i in range(len(s)):
        segment = s[i : m + i]
        if len(segment) == m and sum(segment) == d:
            n_segments += 1
    return n_segments


def test_birthday():
    """Test for birthday function."""
    assert birthday(s=[2, 2, 1, 3, 2], d=4, m=2) == 2
    assert birthday(s=[1, 2, 1, 3, 2], d=3, m=2) == 2
    assert birthday(s=[1, 1, 1, 1, 1, 1], d=3, m=2) == 0
    assert birthday(s=[4], d=4, m=1) == 1


test_birthday()
n = int(input().strip())
s = list(map(int, input().rstrip().split()))
dm = input().rstrip().split()
d = int(dm[0])
m = int(dm[1])
result = birthday(s, d, m)
print(result)
