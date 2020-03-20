# Problem Title: X of a Kind in a Deck of Cards
class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        d = {}
        N = len(deck)
        for card in deck:
            if card in d:
                d[card] += 1
            else:
                d[card] = 1
        for divider in range(2, N+1):
            if N % divider == 0:
                if all(d[v] % divider == 0 for v in d):
                    return True
        return False

