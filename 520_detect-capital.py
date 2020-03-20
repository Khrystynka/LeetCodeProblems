# Problem Title: Detect Capital
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word == word.lower():
            return True

        if word[0] == word[0].lower():
            return False
        if word[1:] == word[1:].lower() or word[1:] == word[1:].upper():
            return True

