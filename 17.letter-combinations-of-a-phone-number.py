#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
from collections import deque


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return ""

        keypad = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        queue = deque(keypad[digits[0]])

        for d in digits[1:]:
            curLevel = []
            for _ in range(len(queue)):
                popped = queue.popleft()
                for v in keypad[d]:
                    curLevel.append(popped + v)

            queue.extend(curLevel)

        return queue

# @lc code=end
