# Problem Title: Word Break
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordDict = set(wordDict)
        self.memo = {}

        def helper(subs):
            if subs in self.memo:
                return self.memo[subs]
            if subs in wordDict or subs == '':
                self.memo[subs] = True
                return True
            res = False
            for i in range(len(subs)):
                if subs[:i+1] in wordDict:
                    res = res or helper(subs[i+1:])
            self.memo[subs] = res
            return res
        return helper(s)

