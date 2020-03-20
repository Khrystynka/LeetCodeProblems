# Problem Title: Binary Watch
from itertools import combinations


class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """

        def convertToTime(lst):

            if lst[0] == ():
                s1 = '0'
            else:
                s = (sum(lst[0]))

                if s >= 12:
                    return ''
                else:
                    s1 = str(s)

            if lst[1] == ():
                s2 = '00'
            else:
                s = (sum(lst[1]))
                if s >= 60:
                    return ''
                elif s >= 10:
                    s2 = str(s)
                else:
                    s2 = "0"+str(s)
            return s1+':'+s2

        hours = (1, 2, 3, 4)
        minutes = tuple(range(1, 7))
        d_hours = {1: 1, 2: 2, 3: 4, 4: 8}
        d_minutes = {1: 1, 2: 2, 3: 4, 4: 8, 5: 16, 6: 32}
        time_list = []

        for k in range(0, min(4, num)+1):
            hours_k = list(combinations(hours, k))
            minutes_k = list(combinations(minutes, num-k))
            for el1 in hours_k:
                for el2 in minutes_k:
                    time = convertToTime(
                        [tuple(map(lambda x:d_hours[x], el1)), tuple(map(lambda x: d_minutes[x], el2))])
                    if time != '':
                        time_list.append(time)
        return time_list

