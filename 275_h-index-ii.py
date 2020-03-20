# Problem Title: H-Index II
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        start = 0
        end = n-1
        while end >= start:
            mid = (end+start)/2
            if citations[mid] == (n-mid):
                return n-mid
            elif citations[mid] > (n-mid):
                end = mid-1
            else:
                start = mid+1
        return n-start

