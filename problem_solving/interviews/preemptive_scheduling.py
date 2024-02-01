#!/bin/python3

import os


#
# Complete the 'getTotalExecutionTime' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY logs
#


def getTotalExecutionTime(n, logs):
    # Write your code here
    # It should return an array of size n, and the element at index i
    # should be the total execution time of function i
    # logs = ["0:start:0"]
    runtimes = [0] * n
    # runtimes[1] +=
    currently_running = None
    previous_timestamp = 0

    # stack
    preempted_functions = []

    for line in logs:
        # line = "0:start:0"
        tokens = line.split(":")
        function_id = int(tokens[0])
        action = tokens[1]
        current_timestamp = int(tokens[2])

        # print(line)
        # print(currently_running)

        if action == "start" and currently_running != function_id:
            # is it first function to run ?
            if currently_running is not None:
                # preempt currently running function
                preempted_functions.append(currently_running)

                # add runtime to runtimes
                runtimes[currently_running] += (
                    current_timestamp - previous_timestamp
                )

            # update currently running function
            currently_running = function_id

            previous_timestamp = current_timestamp

        if action == "end" and currently_running == function_id:
            # calculate runtime
            runtimes[currently_running] += (
                current_timestamp + 1 - previous_timestamp
            )

            # is it last function to run ?
            if len(preempted_functions) != 0:
                # restart the preempted function
                currently_running = preempted_functions.pop()
            else:
                # reset currently running
                currently_running = None

            # preempting happened at the end
            previous_timestamp = current_timestamp + 1

    return runtimes


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    logs_count = int(input().strip())

    logs = []

    for _ in range(logs_count):
        logs_item = input()
        logs.append(logs_item)

    result = getTotalExecutionTime(n, logs)

    fptr.write("\n".join(map(str, result)))
    fptr.write("\n")

    fptr.close()
