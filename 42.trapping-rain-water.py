#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        i_max = height[i]
        j_max = height[j]
        res = 0

        while i < j:
            if height[i] < height[j]:
                i += 1
                i_max = max(i_max, height[i])
                res += i_max - height[i]
            else:
                j -= 1
                j_max = max(j_max, height[j])
                res += j_max - height[j]

        return res
        
# @lc code=end