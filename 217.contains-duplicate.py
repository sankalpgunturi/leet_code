class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        my_set = set()
        for i in nums:
            if i not in my_set:
                my_set.add(i)
            else:
                return True
        
        return False
        
