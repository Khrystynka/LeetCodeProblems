# Problem Title: Palindrome Number
class Solution(object):
    def isPalindrome(self, x):
        if 0 <= x and x < 10:
            return True

        if x < 0 or not x % 10:
            return False
        rev_x = -1
        while rev_x < x:
            if rev_x == -1:
                rev_x_next = x % 10
            else:
                rev_x_next = rev_x*10+x % 10
            x = x/10
            if rev_x_next == x or rev_x == x:
                return True
            rev_x = rev_x_next
        return False

