# Problem Title: Remove Linked List Elements

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        node = head
        prev = head
        while node != None:
            if node.val == val:
                if node == head:
                    head = node.next
                else:
                    prev.next = node.next
                node = node.next
            else:

                prev = node
                node = node.next
        return head

