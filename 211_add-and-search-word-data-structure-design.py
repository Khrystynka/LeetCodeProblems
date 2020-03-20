# Problem Title: Add and Search Word - Data structure design

class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.wordEnd = False


class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        node = self.root
        for letter in word:
            if letter in node.children:
                node = node.children[letter]
            else:
                new_node = TrieNode()
                node.children[letter] = new_node
                node = new_node
        node.wordEnd = True

    def dfs(self, word, node):
        # print word, node.children.keys()
        if word == '':
            return node.wordEnd == True
        letter = word[0]
        if letter in node.children:
            return self.dfs(word[1:], node.children[letter])
        elif letter == '.':
            for next_letter in node.children:
                if self.dfs(word[1:], node.children[next_letter]):
                    return True

    def search(self, word):
        node = self.root
        return self.dfs(word, node)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

