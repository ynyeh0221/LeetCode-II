/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    let n = nums.length;
    if (n === 0)
        return 0;
    else if (n === 1)
        return nums[0];
    else if (n === 2)
        return Math.max(nums[0], nums[1]);
    let T = [];
    for (let i = 0; i < n; i++)
        T.push(0);
    T[0] = nums[0];
    T[1] = Math.max(nums[0], nums[1]);
    for (let i = 2; i < n; i++)
        T[i] = Math.max(T[i-1], T[i-2] + nums[i]);
    return T[n-1];
};
