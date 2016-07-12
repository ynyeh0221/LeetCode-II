class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == 0:
                temp = nums.pop(i)
                nums.insert(0,temp)
            elif nums[i] == 2:
                temp = nums.pop(i)
                nums.append(temp)
                i -= 1
                n -= 1
            i += 1
