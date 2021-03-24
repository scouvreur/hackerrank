#!/bin/python3

import os


# Complete the sockMerchant function below.
def sockMerchant(n, array):
    counts = {}
    for item in array:
        try:
            counts[item] += 1
        except KeyError:
            counts.update({item: 1})

    n_pairs = 0
    for key in counts.keys():
        n_pairs += counts[key] // 2
    return n_pairs


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")
    n = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)
    fptr.write(str(result) + "\n")
    fptr.close()
