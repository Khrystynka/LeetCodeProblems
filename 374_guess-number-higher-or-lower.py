# Problem Title: Guess Number Higher or Lower
class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        r = n
        while r >= l:
            mid = l+(r-l)/2
            res = guess(mid)

            if res == 0:
                return mid
            elif res == -1:
                r = mid-1
            else:
                l = mid+1

