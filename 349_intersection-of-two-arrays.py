# Problem Title: Intersection of Two Arrays
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        def set_intersection(set1, set2):
            res = []
            for el in set1:
                if el in set2:
                    res.append(el)
            return res
        n = len(nums1)
        m = len(nums2)
        if n == 0 or m == 0:
            return []
        set1 = set(nums1)
        set2 = set(nums2)
        if n <= m:
            return set_intersection(set1, set2)
        else:
            return set_intersection(set2, set1)

