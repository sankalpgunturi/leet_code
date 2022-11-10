#
# @lc app=leetcode id=399 lang=python3
#
# [399] Evaluate Division
#

# @lc code=start
from collections import defaultdict


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        division = defaultdict()
        # {
        #     ("a", "b") = 1.5
        #     ("b", "c") = 2.5
        #     ("bc", "cd") = 5.0
        # }

        for i in range(len(equations)):
            division[tuple(equations[i])] = values[i]

        for i in range(len(queries)):
            queries[i][0]


        # print(division)




# @lc code=end
