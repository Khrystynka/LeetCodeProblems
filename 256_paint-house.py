# Problem Title: Paint House
class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        current = [0, 0, 0]
        for cost in costs:
            prev = current
            current = []
            current.append(cost[0]+min(prev[1], prev[2]))
            current.append(cost[1]+min(prev[0], prev[2]))
            current.append(cost[2]+min(prev[0], prev[1]))
        return min(current)

