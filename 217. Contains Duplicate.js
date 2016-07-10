/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    var dic = {};
    for (var i = 0; i < nums.length; i++)
    {
        if (!(nums[i] in dic))
            dic[nums[i]] = 1;
        else
            return true;
    }
    return false;
};
