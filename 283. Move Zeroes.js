/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
    var ind = 0;
    var n = nums.length;
    for (var i = 0; i < n; i++)
    {
        if (nums[i] !== 0)
        {
            nums[ind] = nums[i];
            ind += 1;
        }
    }
    for (i = ind; i < n; i++)
        nums[i] = 0;
};
