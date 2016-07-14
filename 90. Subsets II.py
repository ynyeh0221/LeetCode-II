class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        res = set()
        for k in xrange(len(nums)+1):
            self.DFS(res, [], 0, nums, k)
        return list(res)
        
    def DFS(self, res, path, start, nums, k):
        if len(path) == k:
            res.add(tuple(path))
            return
        for i in xrange(start, len(nums)):
            self.DFS(res, path + [nums[i]], i+1, nums, k)
