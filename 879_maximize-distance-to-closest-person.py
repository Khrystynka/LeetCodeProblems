# Problem Title: Maximize Distance to Closest Person
class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        n = len(seats)
        dp = [0]*n
        prev = -1
        for i in range(n):
            if seats[i] == 1:
                for j in range(prev+1, i):
                    dp[j] = min(i-j, j-prev) if prev >= 0 else i-j
                prev = i

        for j in range(prev+1, n):
            dp[j] = j-prev
        print dp
        return max(dp)

