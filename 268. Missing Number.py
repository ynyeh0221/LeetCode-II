class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        res = 0
        for i in xrange(1, n+1):
            res ^= i
        for i in nums:
            res ^= i
        return res
