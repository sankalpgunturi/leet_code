#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#

# @lc code=start
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def recurseThroughIsland(i, j):
            grid[i][j] = 0
            neighbours = {
                (i+1, j),
                (i-1, j),
                (i, j+1),
                (i, j-1)
            }

            sum = 0
            for i, j in neighbours:
                if i >= 0 and j >= 0 and i < m and j < n and grid[i][j] == 1:
                    sum += recurseThroughIsland(i, j)

            return sum + 1

        area = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    temp = recurseThroughIsland(i, j)
                    if area < temp:
                        area = temp

        return area
# @lc code=end
