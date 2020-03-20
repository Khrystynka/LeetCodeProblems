# Problem Title: Zigzag Iterator
class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.v1 = v1
        self.v2 = v2
        self.p1 = 0
        self.p2 = 0
        self.n1 = len(v1)
        self.n2 = len(v2)
        self.first = True

    def next(self):
        """
        :rtype: int
        """
        if (self.first and self.p1 < self.n1) or self.p2 >= self.n2:
            self.first = False
            res = self.v1[self.p1]
            self.p1 += 1
        else:
            self.first = True
            res = self.v2[self.p2]
            self.p2 += 1
        return res

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.p1 >= self.n1 and self.p2 >= self.n2:
            return False
        return True

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())

