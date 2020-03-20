# Problem Title: To Lower Case
class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        arr = []
        for char in str:
            if 90 >= ord(char) >= 65:
                arr.append(chr(ord(char)+32))
            else:
                arr.append(char)
        return ''.join(arr)

