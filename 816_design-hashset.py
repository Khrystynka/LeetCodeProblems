# Problem Title: Design HashSet
class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 10000
        self.hash = [[None]]*self.size

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        ind = key % self.size
        if self.hash[ind] == [None]:
            self.hash[ind] = [key]
        else:
            self.hash[ind].append(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        ind = key % self.size
        for i in range(len(self.hash[ind])):
            if self.hash[ind][i] == key:
                self.hash[ind][i] = None

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        ind = key % self.size
        if key in self.hash[ind]:
            return True
        else:
            False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

