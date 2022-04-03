# Source: https://leetcode.com/problems/roman-to-integer/discuss/1907667/Python-easy-to-read-solution-O(n)
# Come back to this problem, after reading maps.

class Solution:
    def __init__(self):
        self.map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    def romanToInt(self, roman: str) -> int:
        acc_sum = 0
        prev_num = 0

        # iterate in reverse order
        for single_roman in roman[::-1]:
            num = self.map[single_roman]
            acc_sum += num if prev_num <= num else -num  # roman number feature 
            prev_num = num

        return acc_sum