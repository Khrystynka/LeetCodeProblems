# Problem Title: Convert Sorted List to Binary Search Tree
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None

        def size(node):
            i = 0
            while node:
                i += 1
                node = node.next
            return i
        print size(head), head.val
        self.head = head

        def buildSubTree(l, r):
            if l > r:
                return None
            mid = (l+r)/2
            left = buildSubTree(l, mid-1)
            root = TreeNode(self.head.val)
            self.head = self.head.next
            root.left = left
            root.right = buildSubTree(mid+1, r)
            return root
        return buildSubTree(0, size(head)-1)

