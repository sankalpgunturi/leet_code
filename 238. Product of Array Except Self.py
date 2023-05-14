class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = [1] * len(nums)
        for i, n in enumerate(nums):
            j = 0
            if i == j:
                j += 1
            while i != j and j < len(answer):
                answer[j] = answer[j] * n
                j += 1
                if i == j:
                    j += 1
        
        return answer
