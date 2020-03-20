# Problem Title: Next Greater Element I
from collections import defaultdict


class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        d = defaultdict(lambda: -1)
        for i in range(0, len(nums2)):
            j = i+1
            while j < len(nums2) and nums2[i] > nums2[j]:
                j = j+1
            if j < len(nums2):
                d[nums2[i]] = nums2[j]
        return [d[x] for x in nums1]

