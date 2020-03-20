# Problem Title: H-Index
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        max_h = 0
        citations = sorted(citations)
        n = len(citations)
        for i in range(n-1, -1, -1):
            if citations[i] >= n-i:
                max_h = n-i
            else:
                # if citations[i]==citations[i+1]:
                #max_h= 0
                # else:
                return max_h
        return max_h

