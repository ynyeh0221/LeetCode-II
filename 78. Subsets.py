class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        for k in xrange(len(nums)+1):
            self.DFS(res, [], 0, nums, k)
        return res
        
    def DFS(self, res, path, start, nums, k):
        if len(path) == k:
            res += [path[:]]
            return
        for i in xrange(start, len(nums)):
            self.DFS(res, path + [nums[i]], i+1, nums, k)
