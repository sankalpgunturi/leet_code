#
# @lc app=leetcode id=221 lang=python3
#
# [221] Maximal Square
#

# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        def recursion(i, j):
            matrix[i][j] = "0"
            neighbours = {
                (i, j+1),
                (i+1, j),
                (i+1, j+1)
            }

            sum = 0
            for i, j in neighbours:
                if i < m and j < n and i >= 0 and j >= 0 and matrix[i][j] == "1":
                    sum += recursion(i, j)

            return sum + 1

        area = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    temp = recursion(i, j)
                    if area < temp:
                        area = temp

        return area


# @lc code=end
