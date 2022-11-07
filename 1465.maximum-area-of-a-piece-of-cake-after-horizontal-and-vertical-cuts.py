#
# @lc app=leetcode id=1465 lang=python3
#
# [1465] Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts
#

# @lc code=start
class Solution:
    def findDifferenceBetweenCuts(self, a, b):
        return abs(a - b)

    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()

        max_vertical_difference = 0
        max_horizontal_difference = 0

        max_vertical_difference = self.findDifferenceBetweenCuts(
            0, verticalCuts[0])
        for i in range(0, len(verticalCuts) - 1):
            max_vertical_difference = max(
                max_vertical_difference, self.findDifferenceBetweenCuts(verticalCuts[i], verticalCuts[i + 1]))
        max_vertical_difference = max(
            max_vertical_difference, self.findDifferenceBetweenCuts(verticalCuts[-1], w))

        max_horizontal_difference = self.findDifferenceBetweenCuts(
            0, horizontalCuts[0])
        for i in range(0, len(horizontalCuts) - 1):
            max_horizontal_difference = max(
                max_horizontal_difference, self.findDifferenceBetweenCuts(horizontalCuts[i], horizontalCuts[i + 1]))
        max_horizontal_difference = max(
            max_horizontal_difference, self.findDifferenceBetweenCuts(horizontalCuts[-1], h))

        return int((max_vertical_difference * max_horizontal_difference) % 1000000007)
# @lc code=end
