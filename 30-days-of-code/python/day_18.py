class Solution:
    """
    Stack and queue implementation
    """

    def __init__(self):
        self.stack = []
        self.queue = []

    def check_input(self, char):
        if len(char) > 1:
            raise ValueError

    def pushCharacter(self, char):
        self.check_input(char)
        return self.stack.append(char)

    def popCharacter(self):
        return self.stack.pop()

    def enqueueCharacter(self, char):
        self.check_input(char)
        return self.queue.append(char)

    def dequeueCharacter(self):
        return self.queue.pop(0)


# read the string s
s = input()
# test cases
s = "racecar"  # should return Yes
s = "yes"  # shoudl return No

# Create the Solution class object
obj = Solution()

# push/enqueue all the characters of string s to stack
for i in range(len(s)):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome = True
"""
pop the top character from stack
dequeue the first character from queue
compare both the characters
"""
for i in range(len(s) // 2):
    if obj.popCharacter() != obj.dequeueCharacter():
        isPalindrome = False
        break
# finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, " + s + ", is a palindrome.")
else:
    print("The word, " + s + ", is not a palindrome.")
