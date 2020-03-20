# Problem Title: Fizz Buzz
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = [str(i+1) for i in range(0, n)]

        def repeat(res, k, n, word):
            k = k
            i = k-1
            while i < n:
                res[i] = word
                i += k

        repeat(res, 3, n, 'Fizz')
        repeat(res, 5, n, 'Buzz')
        repeat(res, 15, n, 'FizzBuzz')

        return res

