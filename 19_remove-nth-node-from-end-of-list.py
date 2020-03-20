# Problem Title: Remove Nth Node From End of List
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        new_head = ListNode(None)
        new_head.next = head
        i = new_head
        j = new_head

        while n >= 0:
            j = j.next
            n -= 1
        while j != None:
            j = j.next
            i = i.next
        i.next = i.next.next
        return new_head.next

