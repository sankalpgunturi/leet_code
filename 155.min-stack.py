#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
class MinStack:

    def __init__(self):
        self.min = float("inf")
        self.stack = []
        
    def push(self, val: int) -> None:
        if(val < self.min):
            self.min = val
        
        self.stack.append([val, int(self.min)])

    def pop(self) -> None:
        self.stack.pop()
        if(self.stack):
            self.min = self.stack[-1][1]
        else:
            self.min = float("inf")
        
    def top(self) -> int:
        return self.stack[-1][0]
        
    def getMin(self) -> int:
        return self.stack[-1][1]

# [9, 8, 9, 1, 0, 0, 0, 2]
# stack = [[9, 9], [8, 8]]

# [null,null,null,null,2147483647,null,2147483646,null,2147483646,null,null,2147483647,2147483646,null,-2147483648,-2147483648,null,2147483646]
# [null,null,null,null,2147483647,null,2147483646,null,2147483646,null,null,2147483647,2147483647,null,-2147483648,-2147483648,null,2147483647]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

