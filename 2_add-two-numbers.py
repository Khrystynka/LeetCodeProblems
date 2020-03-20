# Problem Title: Add Two Numbers
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        res = dummy
        carry = 0
        while l1 or l2:
            p = l1.val if l1 else 0
            q = l2.val if l2 else 0
            res.next = ListNode((p+q+carry) % 10)
            res = res.next
            carry = (p+q+carry)/10
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
        res.next = ListNode(carry) if carry != 0 else None
        return dummy.next

