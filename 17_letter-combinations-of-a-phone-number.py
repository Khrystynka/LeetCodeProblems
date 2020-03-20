# Problem Title: Letter Combinations of a Phone Number
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        d = {'1': '', '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
             '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        res = []
        if len(digits) < 1:
            return res

        def combination(comb_sofar, rem_digits):
            if rem_digits == '':
                res.append(comb_sofar)
                return
            for letter in d[rem_digits[0]]:
                combination(comb_sofar+letter, rem_digits[1:])

        combination('', digits)
        return res

