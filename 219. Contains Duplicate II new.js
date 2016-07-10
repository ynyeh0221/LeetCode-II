/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    var s = new Set(nums);
    return s.size == nums.length ? false : true;
};
