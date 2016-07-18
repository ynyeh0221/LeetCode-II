# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        pa = headA
        pb = headB
        lengtha = lengthb = 0
        while pa:
            lengtha += 1
            pa = pa.next
        while pb:
            lengthb += 1
            pb = pb.next
        if lengtha > lengthb:
            for i in xrange(lengtha-lengthb):
                headA = headA.next
        else:
            for i in xrange(lengthb-lengtha):
                headB = headB.next
        while headA:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None
