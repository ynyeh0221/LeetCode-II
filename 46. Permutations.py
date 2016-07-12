class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        visited = [False for i in xrange(len(nums))]
        self.DFS([], nums, visited)
        return self.res
        
    def DFS(self, path, nums, visited):
        if len(path) == len(nums):
            self.res += [path[:]]
            return
        for i in xrange(len(nums)):
            if not visited[i]:
                visited[i] = True
                self.DFS(path + [nums[i]], nums, visited)
                visited[i] = False
