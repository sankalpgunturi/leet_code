#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        spiral = []

        i = 0
        j = 0
        while (j < cols):
            spiral.append(matrix[i][j])
            j += 1

        j -= 1
        i += 1
        while (i < rows):
            spiral.append(matrix[i][j])
            i += 1

        i -= 1
        j -= 1
        while (j >= 0):
            spiral.append(matrix[i][j])
            j -= 1

        i -= 1
        j += 1

        # # needs work
        while (i >= 0):
            spiral.append(matrix[i][j])
            i -= 1

        # print(spiral)
        # print("i: ", i)
        # print("j: ", j)
        return spiral

# 00
# 01
# 02
# 12
# 22
# 21
# 20
# 10
# 11


# @lc code=end
