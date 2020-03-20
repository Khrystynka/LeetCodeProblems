# Problem Title: Encode and Decode Strings
class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.

        :type strs: List[str]
        :rtype: str
        """
        res = ''
        for s in strs:
            res += str(len(s))+' '+s
        return res

    def decode(self, s):
        """Decodes a single string to a list of strings.

        :type s: str
        :rtype: List[str]
        """
        # print s
        res = []
        i = 0
        start = 0
        while i < len(s):
            while s[i] != ' ':
                i += 1

            len_s = int(s[start:i])
            res.append(s[i+1:i+1+len_s])
            i = i+len_s+1
            start = i
        return res


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))

