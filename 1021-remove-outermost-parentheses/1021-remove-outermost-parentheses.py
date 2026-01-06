from collections import Counter
class Solution(object):
    def removeOuterParentheses(self, s):
        stack = deque()
        temp = ""
        arr = []
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(s[i])
            else:
                stack.pop()
            temp += s[i]

            if len(stack) == 0:
                temp = temp[1:-1]
                arr.append(temp)
                temp = ""
        return''.join(arr)




