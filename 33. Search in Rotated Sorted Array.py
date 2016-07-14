class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target < nums[0]:
            for i in xrange(len(nums)-1, -1, -1):
                if nums[i] == target:
                    return i
                elif nums[i] < target:
                    return -1
        else:
            for i in xrange(len(nums)):
                if nums[i] == target:
                    return i
                elif nums[i] < nums[0]:
                    return -1
        return -1
