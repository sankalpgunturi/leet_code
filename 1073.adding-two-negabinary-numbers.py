#
# @lc app=leetcode id=1073 lang=python3
#
# [1073] Adding Two Negabinary Numbers
#

# @lc code=start
class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        def convertNegaBinaryToNumber(arr):
            result = 0
            for i in range(len(arr)):
                result += arr[len(arr) - i - 1] * pow(-2, i)
            return result

        def convertNumberToNegaBinary(number):
            arr = []
            while (number):
                arr.append(number & 1)
                number = - (number >> 1)
            return arr[::-1] or [0]

        number_result = convertNegaBinaryToNumber(
            arr1) + convertNegaBinaryToNumber(arr2)
        return convertNumberToNegaBinary(number_result)

# @lc code=end
