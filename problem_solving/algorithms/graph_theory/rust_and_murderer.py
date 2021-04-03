#!/bin/python3


#
# Complete the rust_murdered function below.
#
def rust_murdered(n, roads):
    #
    # Write your code here.
    #
    return None


t = int(input())
for t_itr in range(t):
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    roads = []

    for _ in range(m):
        roads.append(list(map(int, input().rstrip().split())))

    s = int(input())
    result = rust_murdered(n, roads)
    print(" ".join(map(str, result)))
