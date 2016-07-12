class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        T = [0 for i in xrange(n)]
        T[0] = 1
        res = 1
        for i in xrange(1, n):
            temp = 1
            for j in xrange(i):
                if nums[i] > nums[j]:
                    temp = max(temp, T[j] + 1)
            T[i] = temp
            res = max(T[i], res)
        return res
