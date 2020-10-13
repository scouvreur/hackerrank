# n = int(input().strip())
# a = list(map(int, input().strip().split(' ')))

n = 1
a = [4, 3, 2, 1]

# Helper function
def swap(array, k):
    """
    Given an array, function swaps
    item at index k to k+1 and vice
    versa
    """
    tmp = array[k]
    array[k] = array[k + 1]
    array[k + 1] = tmp


def bubble_sort(array):
    """
    Given an array of integers, function
    returns the sorted array
    """
    n_swaps = 0
    for i in range(len(array)):
        for j in range(len(array) - 1):
            if array[j] > array[j + 1]:
                swap(array, j)
                n_swaps += 1
    return array, n_swaps


a, n_swaps = bubble_sort(a)

print("Array is sorted in {} swaps.".format(n_swaps))
print("First Element: {}".format(a[0]))
print("Last Element: {}".format(a[-1]))
