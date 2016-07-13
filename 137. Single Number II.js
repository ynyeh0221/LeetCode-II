/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
    let res = 0;
    for (let i = 0; i < 32; i++)
    {
        let bit = 1 << i, count = 0;
        for (let j = 0; j < nums.length; j++)
            count += bit & nums[j];
        if (count % 3 !== 0)
            res += bit;
    }
    let maxint = Math.pow(2, 31);
    if (res >= maxint)
        res -= 2 * maxint;
    return res;
};
