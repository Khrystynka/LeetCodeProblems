# Problem Title: Word Pattern
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        if pattern == '':
            return str == pattern
        d = {}
        already_used = {}
        str_list = str.split()
        if len(pattern) != len(str_list):
            return False
        for i in range(len(pattern)):
            if pattern[i] in d.keys():
                if d[pattern[i]] != str_list[i]:
                    return False
            else:
                if str_list[i] in already_used.keys():
                    return False
                d[pattern[i]] = str_list[i]
                already_used[str_list[i]] = pattern[i]
        return True

