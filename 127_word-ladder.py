# Problem Title: Word Ladder
from collections import defaultdict, deque


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        L = len(beginWord)
        d = defaultdict(list)
        for word in wordList:
            for i in range(L):

                d[word[:i]+'*'+word[i+1:]] += [word]
        visited = set(beginWord)
        queu = deque([(beginWord, 1)])
        next_words = []
        while queu:
            (word, level) = queu.popleft()
            if word == endWord:
                return level
            next_words = []
            for i in range(L):
                intermid_word = word[:i]+'*'+word[i+1:]
                next_words += (d[intermid_word])
                d[intermid_word] = []
            # print next_words, word
            for word in next_words:

                if word not in visited:
                    visited.add(word)
                    queu.append((word, level+1))
            # print queu
        return 0

