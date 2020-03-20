# Problem Title: Shortest Completing Word
class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        '''res=[]
        d={}
        d1={}

        for char in licensePlate:
            if char.isalpha():
                char=char.lower()
                if char in d:
                    d[char]+=1
                else:
                    d[char]=1
        for word in words:
            for k in d:
                d1[k]=d[k]
            for letter in word:
                if letter in d1:
                    d1[letter]-=1
            if all(d1[k]<=0 for k in d1):
                res.append(word)
        return min(res,key=len)'''
        d = {}
        licensePlate = licensePlate.lower()
        for i in licensePlate:
            if i.isalpha():
                d[i] = licensePlate.count(i)
        l = []
        for word in words:
            print word
            if all(d[i] <= word.count(i) for i in d.keys()):
                l.append(word)
        return sorted(l, key=len)[0]

