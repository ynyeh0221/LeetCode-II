class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        ind = 0
        n = len(nums)
        for i in xrange(n):
            if nums[i] != 0:
                nums[ind] = nums[i]
                ind += 1
        for i in xrange(ind, n):
            nums[i] = 0
