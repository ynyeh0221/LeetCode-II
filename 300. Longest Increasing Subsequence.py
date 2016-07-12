class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        T = [1 for i in xrange(n)]
        res = 1
        for i in xrange(1, n):
            for j in xrange(i):
                if nums[i] > nums[j]:
                    T[i] = max(T[i], T[j] + 1)
            res = max(T[i], res)
        return res
