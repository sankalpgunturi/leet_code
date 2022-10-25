#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
from math import ceil, floor


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        for c in tokens:
            if (len(c) >= 2 and c.startswith("-")):
                if(c.lstrip("-").isdigit()):
                    stack.append(int(c))
            if (c.isdigit()):
                stack.append(int(c))
            elif (c == "+" or c == "-" or c == "/" or c == "*"):
                op1 = stack.pop()
                op2 = stack.pop()
                if (c == "+"):
                    res = op2 + op1
                elif (c == "-"):
                    res = op2 - op1
                elif (c == "/"):
                    res = op2 / op1
                    if (res < 0):
                        res = ceil(res)
                    else:
                        res = floor(res)
                elif (c == "*"):
                    res = op2 * op1
                stack.append(res)
            
        return stack[-1]
# @lc code=end

