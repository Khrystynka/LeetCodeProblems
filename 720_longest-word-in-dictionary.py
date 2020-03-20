# Problem Title: Longest Word in Dictionary
class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        trie = Trie()
        for word in words:
            trie.addword(word)
        return trie.dfs()


class TrieNode(object):
    def __init__(self, full_word=None):
        self.full_word = full_word
        self.terminal = False
        self.children = {}


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def addword(self, word):
        node = self.root
        for letter in word:
            if letter not in node.children:
                node.children[letter] = TrieNode()
            node = node.children[letter]
        node.terminal = True
        node.full_word = word

    def dfs(self):
        res = ''
        stack = []
        if self.root.children == {}:
            return res
        for child in self.root.children:
            stack.append(self.root.children[child])

        while stack:
            node = stack.pop()
            if node.terminal:
                if len(node.full_word) > len(res):
                    res = node.full_word
                elif len(node.full_word) == len(res):
                    res = min(node.full_word, res)

                for child in node.children:
                    stack.append(node.children[child])
        return res

