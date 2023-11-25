from sys import stdin

string = ""
previous_states = []

num_lines = 0
for line in stdin:
    line = line.rstrip()

    if num_lines == 0:
        num_queries = int(line)
    else:
        # 1 - append string
        if line[0] == "1":
            # append previous state
            previous_states.append(string)
            to_append = line.split(" ")[1]
            string += to_append
        # 2 - delete last k characters of string
        elif line[0] == "2":
            # append previous state
            previous_states.append(string)
            k = int(line.split(" ")[1])
            deleted_chars = string[-k:]
            string = string[: len(string) - k]
        # 3 - print the kth character in string
        elif line[0] == "3":
            k = int(line.split(" ")[1])
            print(string[k - 1])
        # 4 - undo last operation
        elif line[0] == "4":
            string = previous_states.pop()

    num_lines += 1
