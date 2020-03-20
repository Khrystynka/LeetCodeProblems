# Problem Title: Number Complement
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        mask = 1
        num_temp = num
        while num_temp != 0:

            num = num ^ mask
            mask = mask << 1
            num_temp = num_temp >> 1
        return num

