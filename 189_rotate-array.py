# Problem Title: Rotate Array
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = 0
        count = 0
        n = len(nums)
        while count < n:
            start_ind = i
            current_ind = start_ind
            next_ind = (current_ind+k) % n
            prev_el = nums[current_ind]
            while next_ind != start_ind:
                temp_el = nums[next_ind]
                nums[next_ind] = prev_el
                current_ind = next_ind
                next_ind = (current_ind+k) % n
                prev_el = temp_el
                count += 1
            i = i+1
            nums[start_ind] = prev_el
            count += 1

