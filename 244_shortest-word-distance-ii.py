# Problem Title: Shortest Word Distance II
class WordDistance(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.words = dict()
        for i, word in enumerate(words):
            if word in self.words:
                self.words[word].append(i)
            else:
                self.words[word] = [i]

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        diff = float('inf')
        lst1 = self.words[word1]
        lst2 = self.words[word2]
        i, j = 0, 0
        while i < len(lst1) and j < len(lst2):
            idx1 = lst1[i]
            idx2 = lst2[j]
            diff = min(diff, abs(idx1-idx2))
            if idx1 > idx2:
                j += 1
            else:
                i += 1
        return diff


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)

