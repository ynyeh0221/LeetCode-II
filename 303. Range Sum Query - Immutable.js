/**
 * @constructor
 * @param {number[]} nums
 */
var NumArray = function(nums) {
    if (nums.length === 0) return;
    this.totalsum = nums;
    for (let i = 1; i < nums.length; i++)
        this.totalsum[i] += this.totalsum[i-1];
};

/**
 * @param {number} i
 * @param {number} j
 * @return {number}
 */
NumArray.prototype.sumRange = function(i, j) {
    return i === 0 ? this.totalsum[j] : this.totalsum[j] - this.totalsum[i-1];
};


/**
 * Your NumArray object will be instantiated and called as such:
 * var numArray = new NumArray(nums);
 * numArray.sumRange(0, 1);
 * numArray.sumRange(0, 2);
 */
