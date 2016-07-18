# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        pf = head.next
        ps = head
        while pf:
            pf = pf.next
            if pf:
                pf = pf.next
            ps = ps.next
            if ps == pf:
                return True
        return False
