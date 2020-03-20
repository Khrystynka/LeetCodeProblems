# Problem Title: Shortest Word Distance
class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        last_idx1 = None
        last_idx2 = None
        diff = float('inf')
        for i, word in enumerate(words):
            if word == word1 or word == word2:
                if word == word1:
                    last_idx1 = i
                else:
                    last_idx2 = i
                if last_idx2 != None and last_idx1 != None:
                    diff = min(diff, abs(last_idx1-last_idx2))
        return diff

