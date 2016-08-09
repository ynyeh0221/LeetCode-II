import random

class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.uni = {}
        self.dic = {}
        self.rem = {}

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.uni:
            self.rem[val] = ''
            self.uni[val] = ''
            self.dic[(val, self.uni[val])] = 1
            self.uni[val] += '*'
            return True
        else:
            self.dic[(val, self.uni[val])] = 1
            self.uni[val] += '*'
            return False

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.uni:
            if self.rem[val] != self.uni[val]:
                del self.dic[(val, self.rem[val])]
                self.rem[val] += '*'
                return True
            else:
                del self.uni[val]
                del self.rem[val]
                return False
        else:
            return False

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        key = random.choice(self.dic.keys())
        return key[0]
