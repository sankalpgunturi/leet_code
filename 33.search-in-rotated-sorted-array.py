#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        mid = 0

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[low]:
                # strictly increasing left half              
                if target < nums[mid] and target >= nums[low]:
                    high = mid
                else:
                    low = mid + 1                 
            else:
                # strictly increasing right half
                if target > nums[mid] and target <= nums[high]:
                    low = mid + 1   
                else:
                    # target < nums[mid] or target > nums[high]
                    high = mid                               

        
        return -1
        
# @lc code=end

