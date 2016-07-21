class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        return self.major(nums)
        
    def major(self, nums):
        if len(nums) == 1:
            return nums[0]
        ml = self.major(nums[:len(nums)/2])
        mr = self.major(nums[len(nums)/2:])
        if nums.count(ml) > len(nums) /2:
            return ml
        else:
            return mr
