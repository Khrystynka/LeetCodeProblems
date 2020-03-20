# Problem Title: Find Smallest Letter Greater Than Target
class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        if target < letters[0] or target >= letters[-1]:
            return letters[0]
        left = 1
        right = len(letters)
        mid = left+(right-left)/2
        while left <= right:
            if letters[mid] > target:
                if letters[mid-1] <= target:
                    return letters[mid]
                else:
                    right = mid-1
            else:
                left = mid+1
            mid = left+(right-left)/2

