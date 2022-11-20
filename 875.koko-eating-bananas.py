#
# @lc app=leetcode id=875 lang=python3
#
# [875] Koko Eating Bananas
#

# @lc code=start
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        h = max(piles)
        val = []
        output = 0

        while (output != h):
            mid = (l + h)//2
            for i in range(len(piles)):
                val[i] = piles[i] // mid
                if piles[i] % mid != 0:
                    output += val[i]
                else:
                    output += val[i] + 1

            if output < h:
                mid = h - 1
            elif output > h:
                mid = l + 1

        return output


# @lc code=end
