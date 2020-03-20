# Problem Title: Ugly Number II
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        heap = []
        heapq.heappush(heap, 1)
        nums = []
        seen = set()
        while len(nums) != n:
            next_el = heapq.heappop(heap)
            nums.append(next_el)
            seen.add(next_el)
            if next_el*2 not in seen:
                seen.add(next_el*2)
                heapq.heappush(heap, next_el*2)
            if next_el*3 not in seen:
                seen.add(next_el*3)
                heapq.heappush(heap, next_el*3)
            if next_el*5 not in seen:
                seen.add(next_el*5)
                heapq.heappush(heap, next_el*5)
        return nums[-1]

