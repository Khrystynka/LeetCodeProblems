# Problem Title: Buddy Strings
class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        def hasdoubles(s):
            s_set = set()
            for i in range(len(s)):
                s_set.add(s[i])
            return len(s) > len(s_set)

        if len(A) != len(B):
            return False
        count = 0
        for i in range(len(A)):
            if A[i] != B[i]:
                count += 1
                if count == 2:
                    if a != B[i] or b != A[i]:
                        return False
                elif count == 1:
                    a = A[i]
                    b = B[i]
                else:
                    return False
        return count == 2 or (count == 0 and hasdoubles(A))

