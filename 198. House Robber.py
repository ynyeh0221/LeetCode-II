class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return nums[0]
        elif n == 2:
            return max(nums[0], nums[1])
        T = [0 for i in xrange(n+1)]
        T[1] = nums[0]
        T[2] = max(nums[0], nums[1])
        for i in xrange(3, n+1):
            T[i] = max(T[i-1], T[i-2] + nums[i-1])
        return T[n]
