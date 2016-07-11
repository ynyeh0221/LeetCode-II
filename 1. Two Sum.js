/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    var dic = {};
    for (var i = 0; i < nums.length; i++)
        dic[nums[i]] = i;
    for (i = 0; i < nums.length; i++)
    {
        if (target - nums[i] in dic && i < dic[target - nums[i]])
            return [i, dic[target - nums[i]]];
    }
};
