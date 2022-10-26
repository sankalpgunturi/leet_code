#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#
import math
# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()

        while n > 1:
            temp = n
            sum = 0
            while temp > 0:
                digit = temp % 10
                temp = temp // 10
                sum += pow(digit, 2)
                
            if sum in visited:
                return False
            
            visited.add(sum)
            n = sum
        
        return True

# @lc code=end

