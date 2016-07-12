class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_achieve = 0
        for i in xrange(len(nums)):
            max_achieve = max(max_achieve, i + nums[i])
            if i < len(nums)-1 and max_achieve < i+1:
                return False
        return True
