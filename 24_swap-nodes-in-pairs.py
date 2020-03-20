# Problem Title: Swap Nodes in Pairs
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        prehead = ListNode(0)
        prehead.next = head
        prev = prehead
        p1 = head
        p2 = head.next
        while p2:
            prev.next = p2
            p1.next = p2.next
            p2.next = p1
            prev = p1
            p1 = p1.next
            p2 = p1.next if p1 else None
        prev.next = p1
        if p1:
            p1.next = None
        return prehead.next

