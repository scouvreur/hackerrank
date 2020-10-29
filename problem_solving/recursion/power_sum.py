#!/bin/python3


def n_root(X: int, N: int) -> float:
    return X**(1/N)


# Complete the power_sum function below.
def power_sum(X: int, N: int) -> int:
    possible_combinations = []
    if int(n_root(X, N)) == n_root(X, N):
        possible_combinations.append([int(n_root(X, N))])
    else:
        pass

    subcombinations = []
    for i in range(int(n_root(X, N)), 0, -1):
        subcombinations.append(i)

    print("possible_combinations =", possible_combinations)
    print("subcombinations =", subcombinations)
    return len(possible_combinations)



def test_power_sum():
    """Test for the power_sum function."""
    assert power_sum(X=13, N=2) == 1
    assert power_sum(X=10, N=2) == 1
    assert power_sum(X=100, N=2) == 3
    assert power_sum(X=100, N=3) == 1


test_power_sum()
X = int(input())
N = int(input())
result = power_sum(X, N)
print(result)
