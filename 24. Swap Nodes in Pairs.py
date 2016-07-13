# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        p = dummy
        nextnode = None
        count = 0
        while head:
            temp = head
            head = head.next
            temp.next = nextnode
            nextnode = temp
            count += 1
            if count == 2 or not head:
                p.next = temp
                p = temp.next
                if p:
                    p.next = None
                nextnode = None
                count = 0
        return dummy.next
