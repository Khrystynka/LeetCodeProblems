# Problem Title: Insertion Sort List
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        def position(node, root):
            head = root.next
            prev = root
            while head and head.val <= node.val:
                prev = head
                head = head.next
            prev.next = node
            node.next = head
            # return root

        start = ListNode(None)
        start.next = head
        prev_val = float('-inf')
        prev_node = start
        while head:
            curr_val = head.val
            if curr_val >= prev_val:
                # print curr_val,prev_val
                prev = head
                prev_val = curr_val
                head = head.next
            else:
                temp = head
                prev.next = head.next
                position(temp, start)
                head = prev.next
        return start.next

