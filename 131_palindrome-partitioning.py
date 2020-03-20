# Problem Title: Palindrome Partitioning
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.memo = dict()

        def ispalindrome(st):
            if st == st[::-1]:
                return True
            return False

        def partition(s=s):
            res = []
            if s == '':
                return [[]]
            if len(s) == 1:
                return [[s]]
            if s in self.memo:
                return self.memo[s]
            for i in range(len(s)):
                print s[:i+1]
                if ispalindrome(s[:i+1]):
                    fixed_part = [s[:i+1]]
                    possible_next = partition(s[i+1:])
                    for next_part in possible_next:
                        res.append(fixed_part+next_part)
            self.memo[s] = res
            return res
        return partition()

