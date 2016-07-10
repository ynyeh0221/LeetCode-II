/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfTwo = function(n) {
    if (n <= 0) return false;
    var temp = Math.log10(n) / Math.log10(2);
    if (Math.round(temp) == temp) return true;
    return false;
};
