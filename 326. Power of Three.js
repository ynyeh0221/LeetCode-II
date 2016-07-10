/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfThree = function(n) {
    if (n <= 0) return false;
    var temp = Math.log10(n) / Math.log10(3);
    if (Math.round(temp) == temp) return true;
    return false;
};
