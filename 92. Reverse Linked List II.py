# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        p = dummy
        for i in xrange(1, m):
            head = head.next
            p = p.next
        nextnode = None
        reverse_end = None
        for i in xrange(m, n+1):
            if i == m:
                reverse_end = head
            temp = head
            head = head.next
            temp.next = nextnode
            p.next = temp
            nextnode = temp
        reverse_end.next = head
        return dummy.next
