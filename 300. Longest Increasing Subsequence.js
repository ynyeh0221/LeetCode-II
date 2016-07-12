/**
 * @param {number[]} nums
 * @return {number}
 */
var lengthOfLIS = function(nums) {
    if (nums.length === 0)
        return 0;
    let T = [];
    for (let i = 0; i < nums.length; i++)
        T.push(1);
    let res = 1;
    for (let i = 1; i < nums.length; i++)
    {
        for (let j = 0; j < i; j++)
        {
            if (nums[i] > nums[j])
                T[i] = Math.max(T[i], T[j] + 1);
        }
        res = Math.max(T[i], res);
    }
    return res;
};
