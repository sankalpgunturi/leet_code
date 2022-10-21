#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxV = float("-inf")
        start = 0
        end = len(height) - 1

        while (start < end):
            curV = min(height[start], height[end]) * (end - start)
            maxV = max(curV, maxV)

            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return maxV

# @lc code=end

