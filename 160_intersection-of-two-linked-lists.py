# Problem Title: Intersection of Two Linked Lists
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        s = set()
        while headA or headB:
            if headA:
                if headA in s:
                    return headA
                else:
                    s.add(headA)
                headA = headA.next

            if headB:
                if headB in s:
                    return headB
                else:
                    s.add(headB)
                headB = headB.next
        return None

