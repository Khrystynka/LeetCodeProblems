# Problem Title: Minimum Index Sum of Two Lists
class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        d = {}
        res = []
        min_val = len(list1)+len(list2)
        for i in range(len(list1)):
            d[list1[i]] = i
        for i in range(len(list2)):
            if list2[i] in d:
                d[list2[i]] += i
                if d[list2[i]] == min_val:
                    res.append(list2[i])
                elif d[list2[i]] < min_val:
                    min_val = d[list2[i]]
                    res = [list2[i]]
        return res

