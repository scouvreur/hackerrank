N = int(input())

list = []
for _ in range(N):
    command = input().rstrip().split()
    if "insert" in command:
        i = int(command[1])
        e = int(command[2])
        list.insert(i, e)
    elif "print" in command:
        print(list)
    elif "remove" in command:
        i = int(command[1])
        list.remove(i)
    elif "append" in command:
        i = int(command[1])
        list.append(i)
    elif "sort" in command:
        list = sorted(list)
    elif "pop" in command:
        list.pop()
    elif "reverse" in command:
        reversed = []
        for _ in range(len(list)):
            reversed.append(list.pop())
        list = reversed
    else:
        None
