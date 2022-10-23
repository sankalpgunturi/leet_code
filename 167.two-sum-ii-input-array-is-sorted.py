#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1
        while(start < end):
            if(target > numbers[end] + numbers[start]):
                start = start + 1
            elif(target < numbers[end] + numbers[start]):
                end = end - 1
            else:
                return [start + 1, end + 1]
        
# @lc code=end