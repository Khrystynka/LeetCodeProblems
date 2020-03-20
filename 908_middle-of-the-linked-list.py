# Problem Title: Middle of the Linked List
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = head
        mid_el = node
        mid_ind = 0
        i = 0
        while node:
            node = node.next
            i = i+1
            if (i)/2 > mid_ind:
                mid_el = mid_el.next
                mid_ind += 1
        return mid_el

