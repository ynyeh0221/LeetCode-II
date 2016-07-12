/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var sortColors = function(nums) {
    let i = 0, n = nums.length;
    while (i < n)
    {
        if (nums[i] === 0)
        {
            nums.splice(i, 1);
            nums.splice(0, 0, 0);
        }
        else if (nums[i] == 2)
        {
            nums.splice(i, 1);
            nums.push(2);
            i -= 1;
            n -= 1;
        }
        i += 1;
    }
};
