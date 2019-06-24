from math import sqrt

def check_prime(n):
    """
    Test for primality of a number
    running in O(√n).

    Parameters
    ----------
    n : int
        Integer to test primality on.
    """
    if n == 1:
        return "Not prime"
    sq = int(sqrt(n))
    for x in range(2, sq+1):
        if n % x == 0:
            return "Not prime"
    return "Prime"

n_tests = int(input())
for _ in range(n_tests):
    n = int(input())
    print(check_prime(n))
