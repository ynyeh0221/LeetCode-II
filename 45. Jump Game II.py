class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        maxjump = [0 for i in xrange(len(nums))]
        maxjump[0] = nums[0]
        for i in xrange(1, len(maxjump)):
            maxjump[i] = max(nums[i] + i, maxjump[i-1])
        i = 0
        res = 0
        while i < len(nums)-1:
            res += 1
            i = maxjump[i]
        return res
