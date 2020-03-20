# Problem Title: Keyboard Row
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        res = []
        row1 = {'q': 1, 'w': 1, 'e': 1, 'r': 1, 't': 1,
                'y': 1, 'u': 1, 'i': 1, 'o': 1, 'p': 1}
        row2 = {'a': 1, 's': 1, 'd': 1, 'f': 1,
                'g': 1, 'h': 1, 'j': 1, 'k': 1, 'l': 1}

        row3 = {'z': 1, 'x': 1, 'c': 1, 'v': 1, 'b': 1, 'n': 1, 'm': 1}
        for word in words:

            valid = True
            if word[0].lower() in row1:
                d = row1
            elif word[0].lower() in row2:
                d = row2
            else:
                d = row3
            for letter in word:
                if letter.lower() not in d:
                    valid = False
                    break
            if valid:
                res.append(word)

        return res

