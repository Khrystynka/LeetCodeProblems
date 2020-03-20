# Problem Title: Simplify Path
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        words = path.split('/')
        for word in words:
            if word == '..':
                if stack:
                    stack.pop()
            elif word != '.' and word != '':
                stack.append(word)
        return '/'+'/'.join(stack)

