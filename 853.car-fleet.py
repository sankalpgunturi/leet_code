#
# @lc app=leetcode id=853 lang=python3
#
# [853] Car Fleet
#

# @lc code=start
from pdb import post_mortem


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = list(zip(position, speed))
        stack = sorted(stack, key=lambda x: x[0])

        numFleets = 0

        while len(stack) > 1:
            top = stack.pop()
            nextTop = stack.pop()

            a, b = top
            c, d = nextTop

            if (d == b and a > c):
                numFleets += 1
                stack.append(nextTop)
                continue

            t = (a - c)/(d - b)
            meetPoint = a + (b * t)

            if t < 0 or meetPoint > target:
                numFleets += 1
                stack.append(nextTop)
            else:
                if (b < d):
                    stack.append((a, b))
                else:
                    stack.append((c, d))

        return numFleets + len(stack)

# @lc code=end
