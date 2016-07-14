class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        pre = nums[0]
        ind = 1
        for i in xrange(1, len(nums)):
            if nums[i] != pre:
                nums[ind] = nums[i]
                ind += 1
                pre = nums[i]
        return ind
