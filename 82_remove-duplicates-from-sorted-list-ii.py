# Problem Title: Remove Duplicates from Sorted List II
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev_val = None
        new_head = None
        valid_node = new_head
        while head:
            if head.val != prev_val and (head.next == None or head.next.val != head.val):
                if not new_head:
                    new_head = head
                    valid_node = new_head
                else:
                    valid_node.next = head
                    valid_node = head
            prev_val = head.val
            head = head.next
        if valid_node:
            valid_node.next = None
        return new_head

