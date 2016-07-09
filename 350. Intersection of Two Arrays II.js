/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersect = function(nums1, nums2) {
    var res = [];
    var i1 = 0;
    var i2 = 0;
    nums1.sort(function(a, b){return a-b});
    nums2.sort(function(a, b){return a-b});
    while (i1 < nums1.length && i2 < nums2.length)
    {
        if (nums1[i1] < nums2[i2])
            i1 += 1;
        else if (nums1[i1] > nums2[i2])
            i2 += 1;
        else if (nums1[i1] == nums2[i2])
        {
            res.push(nums1[i1]);
            i1 += 1;
            i2 += 1;
        }
    }
    return res;
};
