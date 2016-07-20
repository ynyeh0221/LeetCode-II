class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        begin = end = nums[0]
        res = []
        for i in xrange(1, len(nums)):
            if nums[i] > end + 1:
                if begin < end:
                    res += [str(begin) + '->' + str(end)]
                else:
                    res += [str(begin)]
                begin = nums[i]
            end = nums[i]
        if begin < end:
            res += [str(begin) + '->' + str(end)]
        else:
            res += [str(begin)]
        return res
