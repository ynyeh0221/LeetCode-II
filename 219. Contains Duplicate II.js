/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var containsNearbyDuplicate = function(nums, k) {
    var dic = {};
    for (var i = 0; i < nums.length; i++)
    {
        if (!(nums[i] in dic))
            dic[nums[i]] = i;
        else
        {
            if (i - dic[nums[i]] <= k)
                return true;
            dic[nums[i]] = i;
        }
    }
    return false;
};
