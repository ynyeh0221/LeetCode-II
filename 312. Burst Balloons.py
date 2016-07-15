# timeout

class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.DFS(nums)
        
    def DFS(self, nums):
        if len(nums) == 1:
            return nums[0]
        res = 0
        for i in xrange(len(nums)):
            sum = 0
            if i == 0:
                sum = nums[0]*nums[1]
            elif i == len(nums) - 1:
                sum = nums[len(nums) - 1]*nums[len(nums) - 2]
            else:
                sum = nums[i-1] * nums[i] * nums[i+1]
            res = max(res, sum + self.DFS(nums[:i] + nums[i+1:]))
        return res
