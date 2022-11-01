#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start
class Node:
    def __init__(self, x=None, y=None):
        self.key = x
        self.value = y
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.head = Node()
        self.tail = Node()

    def get(self, key: int) -> int:
        temp = self.map[key]
        temp.prev.next = temp.next
        temp.next.prev = temp.prev
        temp2 = self.tail
        self.tail = self.map[key]
        self.tail.prev = temp2
        self.tail.next = None
        return self.map[key]

    def put(self, key: int, value: int) -> None:

        if (key in self.map):
            temp = self.map[key]
            temp.prev.next = temp.next
            temp.next.prev = temp.prev
            self.map[key] = Node(key, value)
            temp2 = self.tail
            self.tail = self.map[key]
            self.tail.prev = temp2
            self.tail.next = None

        else:
            if (len(self.map) < self.capacity):
                temp = self.tail
                self.tail = self.map[key]
                self.tail.prev = temp
                self.tail.next = None

            elif (len(self.map) == self.capacity):
                temp = self.head
                self.head = self.head.next
                temp2 = self.tail
                self.tail = self.map[key]
                del self.map[self.head.key]
                self.tail.prev = temp2
                temp2.next = self.tail
                self.tail.next = None

            # Your LRUCache object will be instantiated and called as such:
            # obj = LRUCache(capacity)
            # param_1 = obj.get(key)
            # obj.put(key,value)
            # @lc code=end

