class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix, postfix, answer = [1] * len(nums), [1] * len(nums), [1] * len(nums)

        for i, n in enumerate(nums):
            t = 0 if i == 0 else i-1
            prefix[i] = n * prefix[t]
        
        l = len(nums) - 1
        for i, n in reversed(list(enumerate(nums))):
            t = l if i == l else i+1
            postfix[i] = n * postfix[t]

        for i in range(len(answer)):
            preval = 1 if i == 0 else prefix[i-1]
            postval = 1 if i == l else postfix[i+1]
            answer[i] = preval * postval

        return answer
        
