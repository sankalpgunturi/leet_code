#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        unique_row = set()
        unique_col = set()
        unique_grid = set()
        for i in range(len(board)):
            unique_row = set()
            unique_col = set()
            for j in range(len(board[i])):
                if board[i][j] in unique_row:
                    return False
                else:
                    unique_row.add(board[i][j])

                if board[j][i] in unique_col:
                    return False
                else:
                    unique_col.add(board[j][i])

        min_counter = 0
        max_counter = 3
        for i in range(min_counter, max_counter):
            unique_grid = set()
            if min_counter <= 7:
                min_counter += 3
            if max_counter <= 9:
                max_counter += 3
            for j in range(0, 3):
                if board[i][j] in unique_grid:
                    return False
                else:
                    unique_grid.add(board[i][j])


# @lc code=end
