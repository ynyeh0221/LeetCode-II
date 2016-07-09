class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1, nums2 = sorted(nums1), sorted(nums2)
        i1, i2 = 0, 0
        res = []
        while i1 < len(nums1) and i2 < len(nums2):
            if nums1[i1] < nums2[i2]:
                i1 += 1
            elif nums1[i1] > nums2[i2]:
                i2 += 1
            elif nums1[i1] == nums2[i2]:
                res += [nums1[i1]]
                i1 += 1
                i2 += 1
        return res
