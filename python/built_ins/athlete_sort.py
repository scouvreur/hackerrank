#!/bin/python3

if __name__ == "__main__":
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    k = int(input())


arr_sorted = sorted(arr, key=lambda x: x[k])

for row in arr_sorted:
    print(" ".join(list(map(str, row))))
