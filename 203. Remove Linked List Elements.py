# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        p = dummy
        while head:
            if head.val == val:
                p.next = head.next
                head = head.next
            else:
                head = head.next
                p = p.next
        return dummy.next
