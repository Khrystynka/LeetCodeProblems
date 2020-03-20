# Problem Title: Palindrome Permutation II
from collections import defaultdict


class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        middle = ''
        d = defaultdict(lambda: 0)
        odd_count = 0
        self.chars = []
        for char in s:
            d[char] += 1
            if d[char] % 2:
                odd_count += 1
            else:
                odd_count = odd_count-1 if odd_count > 0 else odd_count

        if odd_count > 1:
            return []

        for key in d.keys():
            if d[key] % 2:
                middle = key
            self.chars += [key]*(d[key]/2)
        self.n = len(s)
        self.res = []

        def palindrome(s='', middle=middle, chars=self.chars):
            print s, chars
            if len(s) == self.n/2:
                self.res.append(s+middle+s[::-1])
                return
            for i, char in enumerate(chars):
                if i == 0 or char != chars[i-1]:
                    palindrome(s+char, middle, chars[:i]+chars[i+1:])
        palindrome()
        return self.res

