# Problem Title: Linked List Cycle II
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # if not head or not head.next: return None
        visited = set()
        while head and head not in visited:
            visited.add(head)
            head = head.next
        return head

