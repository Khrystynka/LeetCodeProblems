# Problem Title: Can Place Flowers
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 1
        batches_0 = []
        for fl in flowerbed:
            if fl == 0:

                count += 1
            else:
                if count > 2:
                    batches_0.append(count)
                count = 0
        if count > 1:
            batches_0.append(count+1)
        return sum(((x-2)/2 if x % 2 == 0 else (x-2)/2+1 for x in batches_0)) >= n

