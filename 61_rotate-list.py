# Problem Title: Rotate List
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 0 or not head or not head.next:
            return head

        length = 1
        i = 0
        old_tail = head
        while old_tail.next:
            length += 1
            old_tail = old_tail.next
        old_tail.next = head

        new_tail = head
        while i < length-k % length-1:
            new_tail = new_tail.next
            i += 1
        new_head = new_tail.next
        new_tail.next = None
        return new_head

