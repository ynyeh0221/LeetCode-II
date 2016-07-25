class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        T = [0 for i in xrange(target+1)]
        T[0] = 1
        for i in xrange(target+1):
            for j in nums:
                if i + j <= target:
                    T[i+j] += T[i]
        return T[target]
