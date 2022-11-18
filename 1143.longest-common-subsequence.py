#
# @lc app=leetcode id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#

# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        count = 0
        i = 0
        j = 0
        while i < len(text2):
            while j < len(text1):
                if text2[i] == text1[j]:
                    count += 1
                    break
                j += 1
            i += 1

        return count
        
# @lc code=end
