# Problem Title: Bulls and Cows
from collections import defaultdict


class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bull = 0
        cow = 0

        d = defaultdict(lambda: 0)
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bull += 1
            else:
                d[secret[i]] += 1
        for i in range(len(guess)):
            if guess[i] != secret[i]:
                if d[guess[i]] > 0:
                    cow += 1
                    d[guess[i]] -= 1
        return str(bull) + "A"+str(cow)+"B"

