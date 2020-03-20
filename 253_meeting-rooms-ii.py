# Problem Title: Meeting Rooms II
import heapq


class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        endtimes = []
        intervals = sorted(intervals)

        for i in range(len(intervals)):
            if i != 0 and intervals[i][0] >= endtimes[0]:
                heapq.heappop(endtimes)
            heapq.heappush(endtimes, intervals[i][1])
        return len(endtimes)

