#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        counter = 0

        def findConnectedComponents(i, j):
            grid[i][j] = 0
            neighbours = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
            for i, j in neighbours:
                if i >= 0 and i < m and j >= 0 and j < n and grid[i][j] == "1":
                    findConnectedComponents(i, j)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    findConnectedComponents(i, j)
                    counter += 1

        return counter

# @lc code=end
