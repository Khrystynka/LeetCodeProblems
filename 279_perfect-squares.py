# Problem Title: Perfect Squares
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """

        self.ps = [i*i for i in range(1, int(math.sqrt(n))+1)]
        print n, self.ps

        def find_twosum(target=n):
            start = 0
            end = len(self.ps)-1
            while start <= end:
                print self.ps[start], self.ps[end]
                if target < self.ps[start]:
                    return False
                if target-self.ps[start] == self.ps[end]:
                    return True
                elif target-self.ps[start] > self.ps[end]:
                    start += 1
                else:
                    end -= 1

            return False

        def three_sum(target=n):
            for i in range(len(self.ps)):
                if find_twosum(target-self.ps[i]):
                    return True
            return False

        if n in self.ps:
            return 1
        if find_twosum():
            return 2
        if three_sum():
            return 3
        return 4

