# Problem Title: Repeated DNA Sequences
class Solution:
    def findRepeatedDnaSequences(self, s):
        table = {0: 0}
        ret = []
        for index, num in enumerate(s):
            count = s[index:index+10]
            if count in table:
                ret.append(count)
            else:
                table[count] = index
        return list(set(ret))

