/**
 * @param {number} num
 * @return {boolean}
 */
var isPowerOfFour = function(num) {
    if (num <= 0) return false;
    var temp = Math.log10(num) / Math.log10(4);
    if (Math.round(temp) == temp) return true;
    return false;
};
