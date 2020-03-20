# Problem Title: Unique Word Abbreviation
from collections import defaultdict


class ValidWordAbbr(object):

    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        self.d = defaultdict(lambda: set())
        for word in dictionary:
            if len(word) < 3:
                self.d[word].add(word)
            else:
                self.d[word[0]+str(len(word)-2)+word[-1]].add(word)
        print self.d

    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) == 0:
            return True
        if len(word) < 3:
            abbr = word
        else:
            abbr = word[0]+str(len(word)-2)+word[-1]
        if abbr not in self.d or (len(self.d[abbr]) == 1 and word in self.d[abbr]):
            return True
        return False


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)

