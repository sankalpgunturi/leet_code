#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maximum = 0

    def diameterOfBinaryTree(self, root) -> int:
        self.maximum = 0
        def recurse(node):
            if not node:
                return 0

            left_path = self.diameterOfBinaryTree(node.left)
            right_path = self.diameterOfBinaryTree(node.right)

            current_path = left_path + right_path + 1
            self.maximum = max(self.maximum, current_path)

            return max(left_path, right_path) + 1

        recurse(root)
        return self.maximum - 1


# @lc code=end
