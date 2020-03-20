# Problem Title: Non-decreasing Array
class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n == 0:
            return True
        prev = nums[0]
        pivot1 = None
        pivot2 = None
        flag = False

        i = 1
        while i < len(nums):
            if prev > nums[i]:
                if flag:
                    return False
                else:
                    flag = True
                    pivot1 = i-1
                    pivot2 = i
                    if (nums[pivot1] >= nums[pivot1-1] if pivot1 != 0 else 1) and (nums[pivot1] <= nums[pivot2+1] if pivot2 != n-1 else 1):
                        prev = nums[pivot1]
                    elif (nums[pivot2] >= nums[pivot1-1] if pivot1 != 0 else 1) and (nums[pivot2] <= nums[pivot2+1]if pivot2 != n-1 else 1):
                        prev = nums[pivot2]
                    else:
                        return False
                    i = pivot2+1
            else:
                prev = nums[i]
                i += 1
        return True

