# Problem Title: Remove Duplicates from Sorted List

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        start = head
        next = head.next
        while next:
            while next and next.val == head.val:
                head.next = next.next
                next = head.next

            head = next
            next = head.next if head else None
        return start

