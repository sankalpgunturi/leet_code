#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start
# O(1) space, but O(n3) time complexity
class Solution:
    def clear(self, matrix, i, j):
        for k in range(0, len(matrix)):
            if matrix[k][j] != 0:
                matrix[k][j] = None
        for l in range(0, len(matrix[i])):
            if matrix[i][l] != 0:
                matrix[i][l] = None

    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        array = []
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[i])):
                if (matrix[i][j] == 0):
                    self.clear(matrix, i, j)

        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[i])):
                if (matrix[i][j] == None):
                    matrix[i][j] = 0


# @lc code=end

# [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]
