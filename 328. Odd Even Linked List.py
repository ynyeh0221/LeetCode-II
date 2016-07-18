# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return []
        odd = ListNode(-1)
        even = ListNode(-1)
        dummy1 = odd
        dummy2 = even
        n = 1
        while head:
            if n % 2 == 0:
                even.next = head
                even = even.next
            else:
                odd.next = head
                odd = odd.next
            head = head.next
            n += 1
        if dummy2.next:
            odd.next = dummy2.next
            even.next = None
        else:
            odd.next = None
        return dummy1.next
