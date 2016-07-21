class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        T = [1 for i in xrange(len(nums))]
        diff = [0 for i in xrange(len(nums))]
        res = 1
        for i in xrange(1, len(nums)):
            for j in xrange(i):
                if nums[i] != nums[j]:
                    if diff[j] == 0:
                        T[i] = max(T[i], T[j] + 1)
                        if nums[i] > nums[j]:
                            diff[i] = 1
                        else:
                            diff[i] = -1
                    elif diff[j] == 1 and nums[i] < nums[j]:
                        T[i] = max(T[i], T[j] + 1)
                        diff[i] = -1
                    elif diff[j] == -1 and nums[i] > nums[j]:
                        T[i] = max(T[i], T[j] + 1)
                        diff[i] = 1
            res = max(res, T[i])
        return res
