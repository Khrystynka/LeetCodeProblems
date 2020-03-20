# Problem Title: Design HashMap
class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 10000
        self.dict = [[(None, None)]]*self.size

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        substitute = False
        ind = key % self.size
        if self.dict[ind] == [(None, None)]:
            self.dict[ind] = [(key, value)]
        else:
            for i in range(len(self.dict[ind])):
                if self.dict[ind][i][0] == key:
                    self.dict[ind][i] = (key, value)
                    substitute = True
                    break
            if not substitute:
                self.dict[ind].append((key, value))

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        ind = key % self.size

        for (k, val) in self.dict[ind]:
            if k == key:
                return val
        return -1

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        ind = key % self.size
        for i, tup in enumerate(self.dict[ind]):
            if tup[0] == key:
                self.dict[ind].pop(i)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

