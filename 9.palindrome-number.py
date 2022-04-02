import math

class Solution:
    def isPalindrome(self, x: int) -> bool:

        div = 1
        val = 0

        if x < 0:
            return 0
        elif x == 0:
            return 1
            
        while x != val:
            div = div * 10
            val = x % div
            
        div = math.trunc(div / 10)
        
        val = x - (x % 10)
        val2 = math.trunc(x / div)

        if x == val + val2:
            return 1  
        else:
            return 0  
