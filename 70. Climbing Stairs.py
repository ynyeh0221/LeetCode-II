class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1 or n == 2:
            return n
        pre1 = 1
        pre2 = 2
        for i in xrange(3, n+1):
            temp = pre2
            pre2 = pre1 + pre2
            pre1 = temp
        return pre2
