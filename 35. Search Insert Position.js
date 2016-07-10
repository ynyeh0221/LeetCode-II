/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function(nums, target) {
    var l = 0;
    var r = nums.length;
    while (l <= r)
    {
        var mid = (l + r) >> 1;
        if (mid == nums.length)
            return nums.length;
        if (nums[mid] == target)
            return mid;
        else if (nums[mid] > target)
            r = mid - 1;
        else
            l = mid + 1;
    }
    return l;
};
