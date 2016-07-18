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
            return []
        less, largerequal = ListNode(-1), ListNode(-1)
        dummy1, dummy2 = less, largerequal
        while head:
            if head.val < x:
                less.next = head
                less = less.next
            else:
                largerequal.next = head
                largerequal = largerequal.next
            head = head.next
        if dummy2.next:
            less.next = dummy2.next
            largerequal.next = None
        else:
            less.next = None
        return dummy1.next
