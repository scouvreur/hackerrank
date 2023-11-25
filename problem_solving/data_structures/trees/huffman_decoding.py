"""
class Node:
    def __init__(self, freq,data):
        self.freq= freq
        self.data=data
        self.left = None
        self.right = None
"""


# Enter your code here. Read input from STDIN. Print output to STDOUT
def decodeHuff(root, s):
    current_node = root
    decoded = ""

    for index in range(len(s)):
        # case where 1 go right
        if s[index] == "1":
            current_node = current_node.right

        # case where 0 go left
        if s[index] == "0":
            current_node = current_node.left

        # case where leaf node
        if not current_node.left and not current_node.right:
            decoded += current_node.data
            # return to the root
            current_node = root

    print(decoded)
    return
