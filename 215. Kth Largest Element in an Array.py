from random import randint
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.helper(nums, len(nums) - k + 1)
        
    def helper(self, nums, k):
        pivot = nums[randint(0, len(nums)-1)]
        less = []
        equal = []
        larger = []
        for i in nums:
            if i < pivot:
                less += [i]
            elif i > pivot:
                larger += [i]
            else:
                equal += [i]
        if k <= len(less):
            return self.helper(less, k)
        elif k > len(less) and k <= len(less) + len(equal):
            return pivot
        else:
            return self.helper(larger, k - len(less) - len(equal))
