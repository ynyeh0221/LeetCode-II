class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums = sorted(nums)
        visited = [False for i in xrange(len(nums))]
        self.DFS(res, [], nums, visited)
        return res
        
    def DFS(self, res, path, nums, visited):
        if len(path) == len(nums):
            res += [path[:]]
            return
        for i in xrange(len(nums)):
            if i > 0 and nums[i] == nums[i-1] and not visited[i-1]:
                continue
            if not visited[i]:
                visited[i] = True
                self.DFS(res, path + [nums[i]], nums, visited)
                visited[i] = False
