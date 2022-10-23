#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        open = ['{', '[', '(']
        closed = ['}', ']', ')']

        stack = []

        for c in s:
            if (c in open):
                stack.append(c)
            elif (c in closed):
                print(closed.index(c))
                if len(stack) == 0:
                    return False
                if c == '}':
                    if stack[-1] == '{':
                        stack.pop()
                    else:
                        return False
                if c == ']':
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
                if c == ')':
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
        if len(stack) == 0:
            return True

# @lc code=end
