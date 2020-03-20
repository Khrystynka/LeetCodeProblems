# Problem Title: Merge Intervals
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals = sorted(intervals)
        i = 1
        while i < len(intervals):
            if intervals[i][0] <= intervals[i-1][1]:
                intervals[i] = [min(intervals[i][0], intervals[i-1][0]),
                                max(intervals[i-1][1], intervals[i][1])]
                intervals.pop(i-1)
            else:
                i = i+1
        return intervals

