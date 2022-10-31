#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start
class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.prev_dict = {}
        self.head = Node()
        self.tail = self.head

    def get(self, key: int) -> int:

    def put(self, key: int, value: int) -> None:
        if (value in self.prev_dict):
            prev_node = self.prev_dict[value]
            value_node = prev_node.next

            self.

        else:

            # Your LRUCache object will be instantiated and called as such:
            # obj = LRUCache(capacity)
            # param_1 = obj.get(key)
            # obj.put(key,value)
            # @lc code=end
