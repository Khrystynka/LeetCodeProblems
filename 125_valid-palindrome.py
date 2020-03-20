# Problem Title: Valid Palindrome
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        p1 = 0
        p2 = len(s)-1
        while p1 <= p2:
            if s[p1].isalnum():
                if s[p2].isalnum():
                    if (s[p1]) != s[p2]:
                        return False
                    p1 = p1+1
                    p2 = p2-1
                else:
                    p2 = p2-1
            else:
                p1 = p1+1
        return True

