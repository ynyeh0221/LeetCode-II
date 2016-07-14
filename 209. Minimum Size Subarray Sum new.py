import sys
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = 0
        res = sys.maxint
        while r < len(nums):
            if l == r:
                temp = nums[r]
            else:
                temp = sum(nums[l:r+1])
            if temp < s:
                r += 1
            else:
                res = min(res, r-l+1)
                l += 1
        return res if res < sys.maxint else 0
