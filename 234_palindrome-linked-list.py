# Problem Title: Palindrome Linked List
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return True
        if head.next == None:
            return True
        if head.next.next == None:
            return head.val == head.next.val
        size = 0
        node = head
        while node != None:
            size += 1
            node = node.next
        node = head
        node_after = head.next

        for k in range(0, size/2-1):
            if k == 0:
                node_after = node.next
                node.next = None

            temp = node_after.next
            node_after.next = node
            node = node_after
            node_after = temp

        head1 = node

        head2 = node_after.next if size % 2 else node_after
        print head1.val, head2.val
        while head2 != None:
            if head1.val != head2.val:
                return False
            head1 = head1.next
            head2 = head2.next

        return True

