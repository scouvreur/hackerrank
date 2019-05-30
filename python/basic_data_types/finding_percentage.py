def mean(list_nums):
    """
    Takes in a list of integers or floats and returns
    their arithmetic mean.

    Parameters
    ----------
    list_nums : list[int, float]
        List of numbers as integers or floats.
        If any other type is passed, and exception
        is thrown.

    Returns
    -------
    mean : float
        Average of the list of integers or floats.
    """
    cumsum = 0
    for num in list_nums:
        cumsum += num
    mean = cumsum / len(list_nums)
    return mean


n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = mean(scores)
query_name = input()

print("{0:.2f}".format(student_marks[query_name]))
