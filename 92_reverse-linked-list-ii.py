# Problem Title: Reverse Linked List II
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        p1 = head
        p2 = head
        before_p1 = ListNode(0)
        before_p1.next = p1
        for k in range(n-m):
            p2 = p2.next
        for k in range(m-1):
            before_p1 = before_p1.next
            p1 = p1.next
            p2 = p2.next
        temp2 = p1
        temp1 = p2.next
        before = before_p1
        while p1 != temp1:
            after = p1.next
            p1.next = before
            before = p1
            p1 = after
        before_p1.next = p2
        temp2.next = temp1
        return p2 if m == 1 else head

