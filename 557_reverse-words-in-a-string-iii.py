# Problem Title: Reverse Words in a String III
'''class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=list(s)
        s.append(' ')
        start=0
        end=0
        for i in range(len(s)):
            if s[i]==' ':
                if start<end:
                    for j in range(start,start+(end-start)/2):
                        temp=s[j]
                        s[j]=s[start+end-j-1]
                        s[start+end-j-1]=temp

                start=end+1
                end=start
            else:
                end+=1
        return ''.join(s[:-1])'''


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = (s)+' '
        arr = []
        start = 0
        end = 0
        for i in range(len(s)):
            if s[i] == ' ':
                if start < end:
                    rev = (s[start:end])

                    arr.append(rev[::-1])

                start = end+1
                end = start
            else:
                end += 1
        return ' '.join(arr)

