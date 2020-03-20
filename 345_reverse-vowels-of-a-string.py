# Problem Title: Reverse Vowels of a String
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        start = 0
        end = len(s)-1
        d_vovels = {'a': 1, 'o': 1, 'e': 1, 'i': 1, 'u': 1}
        while start < end:
            while start < end and s[start].lower() not in d_vovels.keys():
                start += 1
            while start < end and s[end].lower() not in d_vovels.keys():
                end = end-1
            if start < end:
                s = s[:start]+s[end]+s[start+1:end] + s[start]+s[end+1:]
                start += 1
                end -= 1
        return s

