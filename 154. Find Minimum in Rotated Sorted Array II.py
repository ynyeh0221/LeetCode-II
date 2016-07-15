class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        for i in xrange(1, len(nums)):
            if nums[i] < res:
                return nums[i]
        return res
