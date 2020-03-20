# Problem Title: Find the Celebrity
# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):


class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        possible_celebrity = 0
        for i in range(n):
            if knows(possible_celebrity, i):
                possible_celebrity = i
        for i in range(n):
            if i != possible_celebrity and (not knows(i, possible_celebrity) or knows(possible_celebrity, i)):
                return -1
        return possible_celebrity

