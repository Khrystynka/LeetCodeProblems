# Problem Title: Most Common Word
from string import punctuation
from collections import Counter


class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        d = {}
        max_occr = 0
        max_word = ''
        for c in punctuation:
            paragraph = paragraph.replace(c, ' ')
        word_list = paragraph.lower().split()
        d = Counter(word for word in word_list)
        for key in d:
            if d[key] > max_occr and key not in banned:
                max_word = key
                max_occr = d[key]
        return max_word

