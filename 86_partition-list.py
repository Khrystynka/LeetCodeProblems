# Problem Title: Partition List
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return head
        smaller_lst_head = ListNode(0)
        curr_node_smalllst = smaller_lst_head
        big_lst_head = ListNode(0)
        curr_node_biglst = big_lst_head
        while head:
            if head.val < x:
                curr_node_smalllst.next = head
                curr_node_smalllst = head
            else:
                curr_node_biglst.next = head
                curr_node_biglst = head
            head = head.next
        curr_node_smalllst.next = big_lst_head.next
        curr_node_biglst.next = None
        return smaller_lst_head.next

