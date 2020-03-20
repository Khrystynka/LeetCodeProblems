# Problem Title: Sort List
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def mergeLst(l1, l2):
            if not l1:
                return l2
            if not l2:
                return l1
            if l1.val >= l2.val:
                l1, l2 = l2, l1
            start = l1
            prev = l1
            while l1 and l2:
                if l1.val <= l2.val:
                    while l1 and l1.val <= l2.val:
                        prev = l1
                        l1 = l1.next
                prev.next = l2
                temp = l2.next
                prev.next.next = l1
                prev = l2
                l2 = temp
            if l2:
                prev.next = l2
            return start

        def MergeSort(head):
            if not head or not head.next:
                return head
            slow = head
            fast = head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            l2 = slow.next
            slow.next = None
            # print l2.val if l2 else None
            # print slow.val
            # print '------'
            l1 = MergeSort(head)
            l2 = MergeSort(l2)
            return mergeLst(l1, l2)
        return MergeSort(head)

