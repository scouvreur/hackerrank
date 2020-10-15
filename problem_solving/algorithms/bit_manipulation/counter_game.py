#!/bin/python3


def get_closest_power_of_2(n):
    return 2 ** ((n).bit_length() - 1)


def is_power_of_2(n):
    return n == get_closest_power_of_2(n)


# Complete the counter_game function below.
def counter_game(n):
    rounds = 0
    while n != 1:
        if is_power_of_2(n):
            n = int(n / 2)
        else:
            n -= get_closest_power_of_2(n)
        rounds += 1
    if rounds % 2 == 0:
        return "Richard"
    else:
        return "Louise"


def test_get_closest_power_of_2():
    """Test for get_closest_power_of_2 function."""
    assert get_closest_power_of_2(n=132) == 128
    assert get_closest_power_of_2(n=9) == 8


def test_is_power_of_2():
    """Test for is_power_of_2 function."""
    assert is_power_of_2(n=2) is True
    assert is_power_of_2(n=3) is False
    assert is_power_of_2(n=8) is True
    assert is_power_of_2(n=9) is False


def test_counter_game():
    """Test for counter_game function."""
    assert counter_game(n=1) == "Richard"
    assert counter_game(n=6) == "Richard"
    assert counter_game(n=132) == "Louise"
    assert counter_game(n=1560834904) == "Richard"
    assert counter_game(n=1768820483) == "Richard"
    assert counter_game(n=1533726144) == "Louise"
    assert counter_game(n=1620434450) == "Richard"
    assert counter_game(n=1463674015) == "Louise"


test_is_power_of_2()
test_get_closest_power_of_2()
test_counter_game()
t = int(input())
for _ in range(t):
    n = int(input())
    result = counter_game(n)
    print(result)
