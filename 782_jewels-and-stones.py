# Problem Title: Jewels and Stones
class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        set_J = set()
        for letter in J:
            set_J.add(letter)
        count = 0
        for letter in S:
            if letter in set_J:
                count += 1
        return count

