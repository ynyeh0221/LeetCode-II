/**
 * @param {number[]} nums
 * @return {number}
 */
var findMin = function(nums) {
    let res = nums[0];
    for (let i = 1; i < nums.length; i++)
    {
        if (nums[i] < res)
            return nums[i];
    }
    return res;
};
