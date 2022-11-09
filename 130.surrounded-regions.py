#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#

# @lc code=start
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        # Flip corner "O" to "Y"
        def recursion(i, j):
            board[i][j] = "Y"
            neighbours = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
            for i, j in neighbours:
                if i >= 0 and i < m and j >= 0 and j < n and board[i][j] == "O":
                    recursion(i, j)

        for i in range(n):
            if board[0][i] == "O":
                recursion(0, i)
            if board[-1][i] == "O":
                recursion(m-1, i)

        for j in range(m):
            if board[j][0] == "O":
                recursion(j, 0)
            if board[j][-1] == "O":
                recursion(j, n-1)

        # Flip all "O" to "X"
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"

        # Flip back all "Y" to "O"
        for i in range(m):
            for j in range(n):
                if board[i][j] == "Y":
                    board[i][j] = "O"


# @lc code=end
