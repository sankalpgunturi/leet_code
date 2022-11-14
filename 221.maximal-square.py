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

        cache = [[0]*n]*m

        def calculatePossibleArea(i, j):
            neighbours = {
                (i+1, j),
                (i, j+1),
                (i+1, j+1)
            }
            perfect_count = 0
            for i, j in neighbours:
                if i >= 0 and j >= 0 and i < m and j < n and matrix[i][j] == "1":
                    perfect_count += 1

            if perfect_count == 3:
                down = calculatePossibleArea(i+1, j)
                right = calculatePossibleArea(i, j+1)
                diag = calculatePossibleArea(i+1, j+1)
                return 1 + min(down, right, diag)
            else:
                return 1

        max_area = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "0":
                    cache[i][j] = 0
                else:
                    cache[i][j] = calculatePossibleArea(i, j)
                    if max_area < cache[i][j]:
                        max_area = cache[i][j]

        return max_area ** 2

# @lc code=end
