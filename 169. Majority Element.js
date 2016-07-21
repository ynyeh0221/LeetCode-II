/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    if (nums.length === 0) return;
    var major = function(nums)
    {
        if (nums.length == 1)
            return nums[0];
        let ml = major(nums.slice(0, nums.length/2)), mr = major(nums.slice(nums.length/2, nums.length));
        let count = 0;
        for (let i = 0; i < nums.length; i++)
        {
            if (nums[i] == ml)
                count += 1;
        }
        if (count > nums.length / 2)
            return ml;
        else
            return mr;
    };
    return major(nums);
};
