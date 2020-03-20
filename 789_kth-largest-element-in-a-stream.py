# Problem Title: Kth Largest Element in a Stream
from heapq import heappushpop, heapify, heappop


class KthLargest(object):
    heap = []
    size = 0

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        nums = sorted(nums, reverse=True)[:k]
        heapify(nums)
        self.heap = nums
        self.size = k
        if len(self.heap) == k:
            self.last = heappop(self.heap)
        else:
            self.last = float('-inf')

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if val <= self.last:
            return self.last
        else:
            self.last = heappushpop(self.heap, val)

        return self.last

