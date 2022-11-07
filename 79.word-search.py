#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
class Solution:
    def __init__(self):
        self.visited_nodes = set()
        self.length_of_chain = 0

    def isTheLetterInTheBoard(self, letter, board):
        for i in range(len(board)):
            for j in range(len(board[i])):
                if letter == board[i][j]:
                    return [i, j, True]
        return [-1, -1, False]

    def checkTheSequenceOfLetters(self, row_index, col_index, word, board):
        self.length_of_chain += 1
        self.visited_nodes.add((row_index, col_index))
        neighbours = [
            # left
            (row_index, col_index - 1),
            # up
            (row_index - 1, col_index),
            # right
            (row_index, col_index + 1),
            # down
            (row_index + 1, col_index)
        ]

        for i, j in neighbours:
            if i >= 0 and j <= 6 and i not in self.visited_nodes and j not in self.visited_nodes:
                next_letter_row_index, next_letter_col_index, present = self.isTheLetterInTheBoard(
                    board[i][j], board)
                if present:
                    self.checkTheSequenceOfLetters(
                        next_letter_row_index, next_letter_col_index, word, board)
            if self.length_of_chain == len(word):
                return True

    def exist(self, board: List[List[str]], word: str) -> bool:
        for letter in word:
            row_index, col_index, present = self.isTheLetterInTheBoard(
                letter, board)
            if not present:
                return False
            else:
                return self.checkTheSequenceOfLetters(row_index, col_index, word, board)


# @lc code=end
