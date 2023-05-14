class Solution(object):



    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        my_map = {}
        for x, number in enumerate(nums):
            difference = target - number
            if difference in my_map:
                return [my_map[difference], x]
            my_map[number] = x
            
