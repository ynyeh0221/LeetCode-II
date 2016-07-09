/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersection = function(nums1, nums2) {
    var used = [];
    for (var i = 0; i < nums2.length; i++)
        used.push(false);
    var res = [];
    for (i = 0; i < nums1.length; i++)
    {
        var temp = nums2.indexOf(nums1[i]);
        if (temp != -1 && used[temp] === false)
        {
            res.push(nums1[i]);
            used[temp] = true;
        }
    }
    return res;
};
