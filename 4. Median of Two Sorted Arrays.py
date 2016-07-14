import random
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total = nums1 + nums2
        if len(total) % 2 != 0:
            return self.median(total, len(total)/2+1)
        else:
            l = self.median(total, len(total)/2)
            r = self.median(total, len(total)/2+1)
            return (l + r) / float(2)
        
    def median(self, nums, k):
        pivot = nums[random.randint(0, len(nums)-1)]
        less = []
        equal = []
        larger = []
        for i in nums:
            if i == pivot:
                equal += [i]
            elif i > pivot:
                larger += [i]
            else:
                less += [i]
        if k <= len(less):
            return self.median(less, k)
        elif k > len(less) and k <= len(less) + len(equal):
            return pivot
        else:
            return self.median(larger, k - len(less) - len(equal))
