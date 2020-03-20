# Problem Title: Sqrt(x)
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x
        left = 1
        right = x/2
        while left <= right:
            mid = (left+right)/2
            if mid*mid <= x:
                if (mid+1)*(mid+1) > x:
                    return mid
                else:
                    left = mid+1
            else:
                right = mid

