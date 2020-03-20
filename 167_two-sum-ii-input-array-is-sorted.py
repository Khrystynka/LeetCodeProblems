# Problem Title: Two Sum II - Input array is sorted
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if numbers == []:
            return []
        i = 0
        j = len(numbers)-1
        start = numbers[i]
        end = numbers[j]
        while i < j:
            while end > target-start and i < j:
                j = j-1
                end = numbers[j]
            if end+start == target:
                return [i+1, j+1]
            else:
                i += 1
                start = numbers[i]
        return []

