class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        ps = nums[0]
        pf = nums[ps]
        while ps != pf:
            pf = nums[nums[pf]]
            ps = nums[ps]
        pf = 0
        while ps != pf:
            pf = nums[pf]
            ps = nums[ps]
        return ps
