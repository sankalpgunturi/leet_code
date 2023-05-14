class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            answer[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in reversed(range(len(nums))):
            answer[i] *= postfix
            postfix *= nums[i]
            
        return answer
