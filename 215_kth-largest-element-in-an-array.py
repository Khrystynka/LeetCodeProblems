# Problem Title: Kth Largest Element in an Array
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        self.n = len(nums)
        self.k = k
        self.idx = self.n-self.k

        def partition(l, r):
            print l, r
            if l == r:
                return nums[l]
            pivot = random.randint(l, r)
            nums[pivot], nums[r] = nums[r], nums[pivot]
            pivot = r
            first_bigger = l
            for i in range(l, r):
                if nums[i] <= nums[pivot]:
                    nums[first_bigger], nums[i] = nums[i], nums[first_bigger]
                    first_bigger += 1
            nums[first_bigger], nums[pivot] = nums[pivot], nums[first_bigger]
            if first_bigger == self.idx:
                return nums[first_bigger]
            if first_bigger < self.idx:
                return partition(first_bigger+1, r)
            else:
                return partition(l, first_bigger-1)
        return partition(0, self.n-1)

