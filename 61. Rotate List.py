# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return []
        length = 1
        p = head
        while p.next:
            p = p.next
            length += 1
        p.next = head
        k %= length
        for i in xrange(length - k):
            p = p.next
        dummy = p.next
        p.next = None
        return dummy
