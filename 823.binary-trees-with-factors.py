#
# @lc app=leetcode id=823 lang=python3
#
# [823] Binary Trees With Factors
#

# @lc code=start
class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        how_many_sub_trees = {}

        for value in arr:
            how_many_sub_trees[value] = 1
            for key in how_many_sub_trees:
                if value % key == 0:
                    possible_factors = value // key
                    if possible_factors in how_many_sub_trees:
                        how_many_sub_trees[value] += how_many_sub_trees[key] * \
                            how_many_sub_trees[possible_factors]

        return int(sum(how_many_sub_trees.values()) % (1e+9 + 7))

# 10e+9 + 7


# @lc code=end
