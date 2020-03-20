# Problem Title: Goat Latin
class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        words_arr = S.split(' ')
        for i, word in enumerate(words_arr):
            if word[0] in ['a', 'e', 'i', 'o', 'u', 'A', "E", 'I', 'O', 'U']:
                words_arr[i] = word+'ma'+'a'*(i+1)
            else:
                words_arr[i] = word[1:]+word[0]+'ma'+'a'*(i+1)
        return ' '. join(words_arr)

