# Problem Title: Flood Fill
class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        row_cnt = len(image)
        col_cnt = len(image[0])
        stack = [(sr, sc)]
        oldColor = image[sr][sc]
        viewed = []
        while stack:
            (r, c) = stack.pop()
            if (r, c) not in viewed:
                viewed.append((r, c))
                image[r][c] = newColor
                if r+1 < row_cnt and image[r+1][c] == oldColor:
                    stack.append((r+1, c))
                if r-1 >= 0 and image[r-1][c] == oldColor:
                    stack.append((r-1, c))
                if c+1 < col_cnt and image[r][c+1] == oldColor:
                    stack.append((r, c+1))
                if c-1 >= 0 and image[r][c-1] == oldColor:
                    stack.append((r, c-1))
        return image

