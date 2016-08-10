import random
class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head. Note that the head is guanranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        p = self.head
        length = res = 0
        while p:
            if random.randint(0, length) == 0:
                res = p
            p = p.next
            length += 1
        return res.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
