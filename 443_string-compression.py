# Problem Title: String Compression
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        # three pointers used

        if len(chars) == 0:
            return 0
        state = chars[0]
        cnt = 0
        pos = 0
        zero = ord('0')
        for c in chars:
            if c == state:
                cnt += 1
            else:
                chars[pos] = state
                pos += 1
                if (cnt > 1):
                    if cnt < 10:
                        chars[pos] = chr(zero + cnt)
                        pos += 1
                    else:
                        for ch in str(cnt):
                            chars[pos] = ch
                            pos += 1
                cnt = 1
                state = c

        chars[pos] = state
        pos += 1
        if (cnt > 1):
            for c in str(cnt):
                chars[pos] = c
                pos += 1

        return pos

