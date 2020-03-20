# Problem Title: Flatten 2D Vector
class Vector2D(object):

    def __init__(self, v):
        """
        :type v: List[List[int]]
        """
        self.vector = v
        self.n = len(self.vector)

        self.i = 0
        while self.i < self.n and self.vector[self.i] == []:
            self.i += 1
        self.j = 0

    def next(self):
        """
        :rtype: int
        """
        res = self.vector[self.i][self.j]
        if self.j >= len(self.vector[self.i])-1:
            self.i += 1
            print self.i
            while self.i < self.n and self.vector[self.i] == []:
                self.i += 1
            self.j = 0
        else:
            self.j += 1
        return res

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.i <= self.n-1 and self.j <= len(self.vector[self.i])-1


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()

