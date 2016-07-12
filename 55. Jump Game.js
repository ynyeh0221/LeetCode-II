/**
 * @param {number[]} nums
 * @return {boolean}
 */
var canJump = function(nums) {
    let max_achieve = 0;
    for (let i = 0; i < nums.length-1; i++)
    {
        max_achieve = Math.max(max_achieve, i + nums[i]);
        if (max_achieve < i+1)
            return false;
    }
    return true;
};
