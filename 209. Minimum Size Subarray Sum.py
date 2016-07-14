# timeout

import sys
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        T = [sys.maxint for i in xrange(len(nums))]
        res = sys.maxint
        for i in xrange(len(nums)):
            for j in xrange(i+1):
                if sum(nums[j:i+1]) >= s:
                    T[i] = min(T[i], i+1-j)
            res = min(res, T[i])
        return res if res < sys.maxint else 0
