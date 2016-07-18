# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return []
        dummy = head
        p = dummy
        head = head.next
        while head:
            if head.val > p.val:
                p.next = head
                p = p.next
            head = head.next
        p.next = None
        return dummy
