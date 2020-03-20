# Problem Title: Two City Scheduling
class Solution(object):
    def twoCitySchedCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """

        costs = sorted(costs, key=lambda x: x[0]-x[1])
        res = sum(x[0] for x in costs[:len(costs)/2])+sum(x[1]
                                                          for x in costs[len(costs)/2:])
        return res

