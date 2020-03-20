# Problem Title: Reorder List
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head: return head    
        start1=head
        end=head
        mid=head
        while  end and  end.next:
            mid=mid.next
            end= end.next.next
        start2=mid.next
        mid.next=None 
        if start2:
            temp= start2.next
            start2.next=None

            while temp:
                temp2=temp.next   
                temp.next=start2
                start2=temp
                temp=temp2
            while  start2:
                temp=start1.next
                start1.next=start2  
                temp2=start2.next
                start2.next=temp
                start1=temp
                start2=temp2'''


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head:
            return None

        s = head
        f = head
        while f and f.next:
            s = s.next
            f = f.next.next
        l2 = self.reverse(s.next)
        s.next = None
        l1 = head

        while l1 and l2:

            tmp1 = l1.next
            tmp2 = l2.next
            l1.next = l2
            l1 = tmp1
            l2.next = l1
            l2 = tmp2

    def reverse(self, node):
        if not node or not node.next:
            return node

        pre = None
        cur = node
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre

