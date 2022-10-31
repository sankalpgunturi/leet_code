#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # O(n) time and O(n) space
        # visited = set()
        # inc = head
        # while (inc not in visited):
        #     if (inc == None):
        #         return False
        #     visited.add(inc)
        #     inc = inc.next

        # return True

        # O(n) time and O(1) space
        fast = head
        slow = head

        while (fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next

            if (slow == fast):
                return True

        return False

# @lc code=end
