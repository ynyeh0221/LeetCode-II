class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in xrange(32):
            count = 0
            bit = 1 << i
            for j in nums:
                count += j & bit
            if count % 3 != 0:
                res += bit
        maxint = 2 ** 31
        if res >= maxint:
            res -= 2 * maxint
        return res
