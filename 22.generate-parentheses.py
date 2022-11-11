#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
from collections import deque


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        queue = deque()
        queue.append(("(", 1, 0))
        res = []

        while queue:
            popped, n_left, n_right = queue.popleft()
            if n_left == n_right == n:
                res.append(popped)
            if n_left < n:
                queue.append((popped+"(", n_left+1, n_right))
            if n_right < n_left:
                queue.append((popped+")", n_left, n_right+1))

        return res


# n = 3
# (, 1, 0
# ()
# ((, 2, 0
# ((), 2, 1
# ("((")
# (()(, 3, 1
# (()(), 3, 2
# ()
# (()()), 3, 3
# res = (()())


# @lc code=end
