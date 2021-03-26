#!/bin/python3

# Complete the kangaroo function below.
def kangaroo(x1: int, v1: int, x2: int, v2: int) -> str:
    # case when kangaroo 2 starts further
    # and moves faster then kangaroo 1
    # it will never catch up
    if (x2 > x1) and (v2 > v1):
        return "NO"
    elif (x2 < x1) and (v2 < v1):
        return "NO"
    else:
        try:
            n_jumps = (x1 - x2) / (v2 - v1)
            if n_jumps == int(n_jumps):
                return "YES"
            else:
                return "NO"
        except ZeroDivisionError:
            return "NO"


def test_kangaroo():
    """Test for kangaroo function."""
    assert kangaroo(x1=0, v1=3, x2=4, v2=2) == "YES"
    assert kangaroo(x1=0, v1=2, x2=5, v2=3) == "NO"
    assert kangaroo(x1=43, v1=2, x2=70, v2=2) == "NO"


test_kangaroo()
x1V1X2V2 = input().split()
x1 = int(x1V1X2V2[0])
v1 = int(x1V1X2V2[1])
x2 = int(x1V1X2V2[2])
v2 = int(x1V1X2V2[3])
result = kangaroo(x1, v1, x2, v2)
print(result)
