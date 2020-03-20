# Problem Title: Shortest Word Distance III
class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        idx1 = None
        idx2 = None
        diff = float('inf')
        for i, word in enumerate(words):
            if word == word1 or word == word2:
                if word == word1:
                    if word1 == word2 and idx1 != None:
                        diff = min(diff, i-idx1)
                    idx1 = i
                else:
                    idx2 = i
                if idx1 != None and idx2 != None:
                    diff = min(diff, abs(idx1-idx2))
        return diff

