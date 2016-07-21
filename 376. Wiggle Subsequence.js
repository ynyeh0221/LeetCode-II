/**
 * @param {number[]} nums
 * @return {number}
 */
var wiggleMaxLength = function(nums) {
    if (nums.length === 0) return 0;
    let T = [], diff = [];
    let res = 1;
    for (let i = 0; i < nums.length; i++)
    {
        T.push(1);
        diff.push(0);
    }
    for (let i = 1; i < nums.length; i++)
    {
        for (let j = 0; j < i; j++)
        {
            if (diff[j] === 0 || (diff[j] > 0 && nums[i] < nums[j]) || (diff[j] < 0 && nums[i] > nums[j]))
            {
                T[i] = Math.max(T[i], T[j] + 1);
                diff[i] = nums[i] - nums[j];
            }
        }
        res = Math.max(res, T[i]);
    }
    return res;
};
