class RandomizedSet(object):

    def __init__(self):
        self.hmap = {}

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if self.hmap.get(val, False):
            return False
        else:
            self.hmap[val] = True
            return True
        
    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        return self.hmap.pop(val, False)

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(list(self.hmap.keys()))

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()