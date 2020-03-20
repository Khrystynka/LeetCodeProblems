# Problem Title: Logical OR of Two Binary Grids Represented as Quad-Trees
'''
LLeetCodeLeetCodeetCode

558. Quad Tree Intersection
Description
Hints
Solution
      
[PyPythonthon]Stupid Approach beats 97% with MORE Examples and Explanation
[Pyton]Stupid Approach beats 97% with MORE Examples and Explanation
13
VIEWS
1
Created at: July 6, 2019 8:26 AM

calvinchankf
calvinchankf
 623
"""
1st1st approach: recursive dfs
- my intuitive approach is just to dfs the trees BUT we need to consider 2 corner cases:
	- e.g.2 a false leaf BUT its counterpart is a QTree
	- e.g.3 all children have the same values
- actually i am not sure what 'val' should i return if it is not a leaf, therefore i put None and leetcode ACCEPTED lol


e.g. 1
A:                 B:                 C (A or B):
+-------+-------+  +-------+---+---+  +-------+-------+
|       |       |  |       | F | F |  |       |       |
|   T   |   T   |  |   T   +---+---+  |   T   |   T   |
|       |       |  |       | T | T |  |       |       |
+-------+-------+  +-------+---+---+  +-------+-------+
|       |       |  |       |       |  |       |       |
|   F   |   F   |  |   T   |   F   |  |   T   |   F   |
|       |       |  |       |       |  |       |       |
+-------+-------+  +-------+-------+  +-------+-------+

e.g.2
A:                 B:                 C (A or B):
+-------+-------+  +-------+---+---+  +-------+-------+
|       |       |  |       | F | F |  |       | F | F |
|   T   |   F   |  |   T   +---+---+  |   T   |---+---+ 
|       |       |  |       | T | T |  |       | T | T |
+-------+-------+  +-------+---+---+  +-------+-------+
|       |       |  |       |       |  |       |       |
|   F   |   F   |  |   T   |   F   |  |   T   |   F   |
|       |       |  |       |       |  |       |       |
+-------+-------+  +-------+-------+  +-------+-------+

e.g.3
A:                 B:                 C (A or B):
+-------+-------+  +-------+---+---+  +-------+-------+
|       |       |  |       |       |  |               |
|   T   |   T   |  |   T   |   T   |  |               |
|       |       |  |       |       |  |               |
+-------+-------+  +-------+---+---+  +       T       ||       |       |  |       |       |  |               |
|   F   |   T   |  |   T   |   T   |  |               |
|       |       |  |       |       |  |               |

'''


class Solution(object):
    def intersect(self, t1, t2):
        if t1.isLeaf and t2.isLeaf:
            return Node(t1.val or t2.val, True, None, None, None, None)
        elif t1.isLeaf:
            if t1.val == True:
                return Node(True, True, None, None, None, None)  # e.g.1
            else:
                return t2  # e.g.2
        elif t2.isLeaf:
            if t2.val == True:
                return Node(True, True, None, None, None, None)  # e.g.1
            else:
                return t1  # e.g.2
        else:
            a = self.intersect(t1.topLeft, t2.topLeft)
            b = self.intersect(t1.topRight, t2.topRight)
            c = self.intersect(t1.bottomLeft, t2.bottomLeft)
            d = self.intersect(t1.bottomRight, t2.bottomRight)
            # e.g.3 if all children have the same value, merge them into one node
            if a.isLeaf and b.isLeaf and c.isLeaf and d.isLeaf:
                # in python2.x, boolean is a subclass of integer
                total = a.val + b.val + c.val + d.val
                if total == 4:
                    return Node(True, True, None, None, None, None)
                elif total == 0:
                    return Node(False, True, None, None, None, None)
            # else, keep 4 children
            return Node(None, False, a, b, c, d)

        """
        :type quadTree1: Node
        :type quadTree2: Node
        :rtype: Node
        """

