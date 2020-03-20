# Problem Title: Reverse Linked List
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        prev_node = None
        next_node = head.next
        while next_node:
            head.next = prev_node
            prev_node = head
            head = next_node
            next_node = head.next
        head.next = prev_node
        return head

