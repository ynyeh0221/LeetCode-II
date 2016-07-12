/**
 * @param {number[]} nums
 * @return {string}
 */
var largestNumber = function(nums) {
    let res = nums.sort((a,b) => a+''+b > b+''+a ? 1 : -1).reverse().join('');
    return res[0] == '0' ? '0' : res;
};
