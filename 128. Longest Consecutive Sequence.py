class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        res = 0
        while nums:
            l = nums.pop()
            r = l
            while l-1 in nums:
                l -= 1
                nums.remove(l)
            while r+1 in nums:
                r += 1
                nums.remove(r)
            res = max(res, r - l + 1)
        return res
