import random

numbers = [5, 10, 10]

numbers = [0, 10, 40, 90, 0, 60, 100, 10, 40, 50, 30, 0]
queries = [[1, 4, 5]]

query_results = []

cumulative_sums = []
cumulative_sum = 0
zeros = []
num_zeros = 0

for number in numbers:
    cumulative_sum += number
    cumulative_sums.append(cumulative_sum)

    if number == 0:
        num_zeros += 1
    zeros.append(num_zeros)


for query in queries:
    start_index = query[0] - 1
    end_index = query[1]
    zero_value = query[2]

    count_zeros = zeros[end_index] - zeros[start_index]
    subarray_sum = 0

    for number in numbers[start_index:end_index]:
        if number == 0:
            count_zeros += 1
        subarray_sum += number

    subarray_sum += count_zeros * zero_value
    query_results.append(subarray_sum)

    # Generate an array of 10 random integers between 1 and 100
    random_numbers = [random.randint(1, 100) for _ in range(10)]

    print(random_numbers)
