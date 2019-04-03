# Enter your code here. Read input from STDIN. Print output to STDOUT
def even_char_string(string):
    # Function takes in a string and returns its even chars
    even_chars = ""
    for i in range(0, len(string)):
        if i%2 == 0:
            even_chars = even_chars + string[i]
    return even_chars

def odd_char_string(string):
    # Function takes in a string and returns its even chars
    odd_chars = ""
    for i in range(0, len(string)):
        if i%2 == 1:
            odd_chars = odd_chars + string[i]
    return odd_chars

num_test_cases = int(input())
strings = []
for i in range(num_test_cases):
    strings.append(str(input()))

for string in strings:
    print(even_char_string(string=string), odd_char_string(string=string))
