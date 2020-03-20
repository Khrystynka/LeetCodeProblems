# Problem Title: Reverse String II
class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """

        arr = list(s)
        for i in range(0, len(arr), 2*k):
            arr[i:i+k] = reversed(arr[i:i+k])

        return ''.join(arr)

