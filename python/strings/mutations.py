def mutate_string(string, position, character):
    temp = []
    for char in string:
        temp.append(char)
    temp[position] = character
    edit_string = ""
    for char in temp:
        edit_string += char
    return edit_string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
