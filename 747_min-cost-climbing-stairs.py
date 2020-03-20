# Problem Title: Min Cost Climbing Stairs
'''class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n=len(cost)
        if n==2:
            return min(cost)
        dp=[0]*n
        dp[0]=cost[0]
        dp[1]=cost[1]
        for i in range(2,n):
            dp[i]=min(dp[i-1],dp[i-2])+cost[i]
        return min(dp[-2],dp[-1])'''


class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        if n == 2:
            return min(cost)
        dp2 = 0
        dp1 = 0
        for i in range(n):
            dp1, dp2 = min(dp1, dp2)+cost[i], dp1
        return min(dp1, dp2)

