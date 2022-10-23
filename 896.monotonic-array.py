#
# @lc app=leetcode id=896 lang=python3
#
# [896] Monotonic Array
#

# @lc code=start
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) <= 2:
            return True

        i = 0
        j = len(nums) - 1
        i_max = nums[i]
        j_max = nums[j]
        res = 0

        while i < j:
            if nums[i] < nums[j]:
                i += 1
                i_max = max(i_max, nums[i])
                res += i_max - nums[i]
            else:
                j -= 1
                j_max = max(j_max, nums[j])
                res += j_max - nums[j]

        return res

        
# @lc code=end

