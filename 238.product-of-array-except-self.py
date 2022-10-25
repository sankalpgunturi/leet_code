#
# @lc app=leetcode id=238 lang=python3
#
# [238] Product of Array Except Self
#

# @lc code=start




class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if(len(nums) == 1):
            return nums

        leftArray = list(nums)
        rightArray = [1] * len(nums)

        for i in range(1, len(nums)):
            leftArray[i] = leftArray[i - 1] * nums[i]

        for i in range(len(nums) - 2, 0, -1):
            rightArray[i] = rightArray[i + 1] * nums[i]

        print(leftArray)
        print(rightArray)

        

        

        
# @lc code=end

