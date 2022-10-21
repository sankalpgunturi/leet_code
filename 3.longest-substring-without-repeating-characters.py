#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visitedChars = set({})
        start = 0
        maxLen = float("-inf")

        for end in range(len(s)):
            while s[end] in visitedChars:
                visitedChars.remove(s[start])
                start += 1

            visitedChars.add(s[end])
            curLen = end - start + 1
            maxLen = max(curLen, maxLen)

        return max(maxLen, 0)

# @lc code=end

