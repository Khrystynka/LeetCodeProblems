# Problem Title: Best Time to Buy and Sell Stock
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfit = 0
        minPrice = float('inf')
        n = len(prices)
        if n < 2:
            return 0
        for i in range(n):
            if (prices[i] < minPrice):
                minPrice = prices[i]
            elif (prices[i]-minPrice) > maxProfit:
                maxProfit = prices[i]-minPrice
        return maxProfit

