# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        en = 0
        dummy = ListNode(-1)
        p = dummy
        while l1 and l2:
            temp = l1.val + l2.val + en
            if temp <= 9:
                p.next = ListNode(temp)
                en = 0
            else:
                p.next = ListNode(temp - 10)
                en = 1
            l1 = l1.next
            l2 = l2.next
            p = p.next
        while l1:
            temp = l1.val + en
            if temp <= 9:
                p.next = ListNode(temp)
                en = 0
            else:
                p.next = ListNode(temp - 10)
                en = 1
            l1 = l1.next
            p = p.next
        while l2:
            temp = l2.val + en
            if temp <= 9:
                p.next = ListNode(temp)
                en = 0
            else:
                p.next = ListNode(temp - 10)
                en = 1
            l2 = l2.next
            p = p.next
        if en == 1:
            p.next = ListNode(1)
        return dummy.next
