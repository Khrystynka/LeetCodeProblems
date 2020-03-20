# Problem Title: Compare Version Numbers
class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        ver1 = version1.split('.')
        ver2 = version2.split('.')
        if len(ver1) > len(ver2):
            ver2 = ver2+['0']*(len(ver1)-len(ver2))
        elif len(ver1) < len(ver2):
            ver1 = ver1+['0']*(len(ver2)-len(ver1))
        for i in range(len(ver1)):
            if int(ver1[i]) > int(ver2[i]):
                return 1
            elif int(ver2[i]) > int(ver1[i]):
                return -1
        return 0

