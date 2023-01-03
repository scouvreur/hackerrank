def is_kaprekar(number):
    digits = len(str(number))
    squared = number ** 2

    digit_sum = 0
    for digit in str(squared):
        digit_sum += int(digit)

    left_digits = str(squared)[0 : len(str(squared)) - digits]
    left = int(left_digits) if left_digits != "" else 0

    right_digits = str(squared)[-digits:]
    right = int(right_digits) if right_digits != "" else 0

    if digit_sum == number:
        return True
    elif left + right == number:
        return True
    else:
        return False


def kaprekar_numbers(lower_bound, upper_bound):
    # Write your code here
    result = []
    for number in range(lower_bound, upper_bound + 1):
        if is_kaprekar(number):
            result.append(number)

    if len(result) == 0:
        print("INVALID RANGE")
    else:
        print(" ".join(list(map(str, result))))
