#
# @lc app=leetcode id=380 lang=python3
#
# [380] Insert Delete GetRandom O(1)
#

# @lc code=start
from random import randint


class RandomizedSet:

    counter: int
    keyToVal: dict
    valToKey: dict

    def __init__(self):
        self.counter = 0
        self.valToKey = {}
        self.keyToVal = {}

    def insert(self, val: int) -> bool:
        if val not in self.valToKey:
            self.keyToVal[self.counter] = val
            self.valToKey[val] = self.counter
            self.counter += 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val not in self.valToKey:
            return False

        keyToRemove = self.valToKey[val]
        del self.keyToVal[keyToRemove]
        del self.valToKey[val]
        return True

    def getRandom(self) -> int:
        randomIndex = randint(0, len(self.keyToVal) - 1)
        randomKey = list(self.keyToVal.keys())[randomIndex]
        return self.keyToVal[randomKey]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end
