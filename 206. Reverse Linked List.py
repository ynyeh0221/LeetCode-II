# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        nextnode = None
        while head:
            temp = head
            head = head.next
            temp.next = nextnode
            dummy.next = temp
            nextnode = temp
        return dummy.next
