# RandomizedSet() Initializes the RandomizedSet object.
# bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
# bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
# int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
# You must implement the functions of the class such that each function works in average O(1) time complexity.
# Example 1:

# Input
# ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
# [[], [1], [2], [2], [], [1], [2], []]
# Output
# [null, true, false, true, 2, true, false, 2]

import random


class RandomizedSet(object):

    def __init__(self):
        self.my_dict = {}
        self.my_list = []

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.my_dict:
            return False
        self.my_dict[val] = len(self.my_list)
        self.my_list.append(val)
        return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.my_dict:
            return False
        # remove element index
        indx = self.my_dict[val]
        last = self.my_list[-1]
        self.my_list[indx] = last
        self.my_dict[last] = indx
        self.my_list.pop()
        del self.my_dict[val]
        return True

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.my_list)


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
print(obj.insert(1))
print(obj.remove(2))
print(obj.insert(2))
print(obj.getRandom())
print(obj.remove(1))
print(obj.insert(2))
print(obj.getRandom())
