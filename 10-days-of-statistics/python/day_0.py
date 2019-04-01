# Enter your code here. Read input from STDIN. Print output to STDOUT

len_numbers = int(input())
numbers = list(map(lambda x: int(x), input().split()))

def mean(numbers):
    """
    Parameters
    ----------
    numbers : list
        a list of numbers

    Returns
    -------
    mean : double
        the mean of the list of numbers passed
    """
    cumsum = 0
    for number in numbers:
        cumsum += number
    mean = cumsum/len(numbers)
    mean = round(mean, 1)
    return mean

def median(numbers):
    """
    Parameters
    ----------
    numbers : list
        a list of numbers

    Returns
    -------
    median : double
        the median of the list of numbers passed
    """
    numbers.sort()
    if len(numbers)%2 == 1:
        median = numbers[-round(-len(numbers)/2)]
        median = round(median, 1)
    else:
        median = (numbers[int(len(numbers)/2)] + numbers[int(len(numbers)/2 -1)])/2
        median = round(median, 1)
    return median

def mode(numbers):
    """
    Parameters
    ----------
    numbers : list
        a list of numbers

    Returns
    -------
    mode : double
        the mode of the list of numbers passed
    """
    counts = {}
    for number in numbers:
        if number in counts.keys():
            counts[number] += 1
        else:
            counts.update({number: 1})
    return max(counts, key=counts.get)


print(mean(numbers))
print(median(numbers))
print(mode(numbers))
