class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i in xrange(len(nums)):
            dic[nums[i]] = i
        for i in xrange(len(nums)):
            if target - nums[i] in dic and i < dic[target - nums[i]]:
                return [i, dic[target - nums[i]]]
