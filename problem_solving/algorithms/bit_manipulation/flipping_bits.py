#!/bin/python3


# Complete the flipping_bits function below.
def flipping_bits(n: int) -> int:
    ref_32_bit = 0b11111111111111111111111111111111
    return n ^ ref_32_bit


def test_flipping_bits():
    """Test for flipping_bits function."""
    assert flipping_bits(n=1) == 4294967294
    assert flipping_bits(n=0) == 4294967295
    assert flipping_bits(n=4) == 4294967291
    assert flipping_bits(n=123456) == 4294843839
    assert flipping_bits(n=35601423) == 4259365872
    assert flipping_bits(n=802743475) == 3492223820
    assert flipping_bits(n=2147483647) == 2147483648


test_flipping_bits()
q = int(input())
for _ in range(q):
    n = int(input())
    result = flipping_bits(n)
    print(result)
