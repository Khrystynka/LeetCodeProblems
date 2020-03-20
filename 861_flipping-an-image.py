# Problem Title: Flipping an Image
class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """

        n = len(A[0])
        for i, row in enumerate(A):
            for j in range((n+1)/2):
                #temp = row[-1-j]
                # row[-1-j]=(row[j])^1
                # row[j]=temp^1
                row[j], row[-1-j] = (row[-1-j]) ^ 1, (row[j]) ^ 1
        return A

