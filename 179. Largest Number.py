def compare(a, b):
    if a+b > b+a:
        return 1
    elif a+b < b+a:
        return -1
    else:
        return 0
            
class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        nums = sorted(map(str, nums), cmp = compare, reverse = True)
        return '0' if nums[0] == '0' else ''.join(nums)
