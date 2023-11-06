from sys import stdin

queue = []
num_lines = 0
for line in stdin:
    line = line.rstrip()

    if num_lines == 0:
        num_queries = int(line)
    else:
        # 1 - enqueue n
        if line[0] == "1":
            n = int(line.split(" ")[1])
            queue.append(n)
        # 2 - dequeue front element
        elif line[0] == "2":
            queue.pop(0)
        # 3 - print the front element
        elif line[0] == "3":
            print(queue[0])

    num_lines += 1
