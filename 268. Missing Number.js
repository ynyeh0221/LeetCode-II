/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
    var res = 0;
    for (var i = 1; i <= nums.length; i++)
        res ^= i;
    for (i = 0; i < nums.length; i++)
        res ^= nums[i];
    return res;
};
