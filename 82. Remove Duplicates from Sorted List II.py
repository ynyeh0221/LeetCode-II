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
        dummy = ListNode(-1)
        p = dummy
        nextadded = head
        head = head.next
        flag = 0
        while head:
            if head.val == nextadded.val:
                flag = 1
            else:
                if flag == 0:
                    p.next = ListNode(nextadded.val)
                    p = p.next
                flag = 0
            nextadded = head
            head = head.next
        if flag == 0 and p.val != nextadded.val:
            p.next = ListNode(nextadded.val)
        return dummy.next
