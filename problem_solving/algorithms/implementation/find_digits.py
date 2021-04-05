# Complete the find_digits function below.
def find_digits(n):
    divisors = 0
    for char in str(n):
        digit = int(char)
        if digit != 0:
            if n % digit == 0:
                divisors += 1
    return divisors


def test_find_digits():
    """Test for find_digits function."""
    assert find_digits(n=124) == 3
    assert find_digits(n=111) == 3
    assert find_digits(n=10) == 1
    assert find_digits(n=12) == 2
    assert find_digits(n=1012) == 3


test_find_digits()
t = int(input())
for t_itr in range(t):
    n = int(input())
    result = find_digits(n)
    print(result)
