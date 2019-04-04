# Enter your code here. Read input from STDIN. Print output to STDOUT

num_entries = int(input())

phone_book = {}
for i in range(num_entries):
    line = str(input()).split()
    phone_book.update({line[0]: int(line[1])})

while True:
    try:
        key = str(input())
        try:
            print("{}={}".format(key, phone_book[key]))
        except KeyError:
            print("Not found")
    except EOFError:
        break
