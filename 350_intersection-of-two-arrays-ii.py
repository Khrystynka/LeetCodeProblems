# Problem Title: Intersection of Two Arrays II
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        def list_intersection(list1, list2):
            res = []
            for el in list1:
                if el in list2:
                    res.append(el)
                    list2.remove(el)
            return res
        n = len(nums1)
        m = len(nums2)
        if n == 0 or m == 0:
            return []
        if n <= m:
            return list_intersection(nums1, nums2)
        else:
            return list_intersection(nums2, nums1)

