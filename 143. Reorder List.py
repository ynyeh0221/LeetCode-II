# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        pf = head
        ps = head
        while pf:
            pf = pf.next
            if pf:
                pf = pf.next
                ps = ps.next
        dummy = ListNode(-1)
        nextnode = None
        mid = ps
        while ps:
            temp = ps
            ps = ps.next
            temp.next = nextnode
            nextnode = temp
            dummy.next = temp
        p = head
        p1 = head.next
        p2 = dummy.next
        while p1 != mid and p2:
            p.next = p2
            p = p.next
            p2 = p2.next
            p.next = p1
            p = p.next
            p1 = p1.next
        while p2:
            p.next = p2
            p = p.next
            p2 = p2.next
