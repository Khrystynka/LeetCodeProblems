# Problem Title: Best Time to Buy and Sell Stock II
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        i = 0
        max_profit = 0
        while i < len(prices)-1:
            if prices[i] < prices[i+1]:
                max_profit += prices[i+1]-prices[i]
            i = i+1
        return max_profit

