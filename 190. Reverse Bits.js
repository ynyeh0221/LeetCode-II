/**
 * @param {number} n - a positive integer
 * @return {number} - a positive integer
 */
var reverseBits = function(n) {
    var bn = (n >>> 0).toString(2).split("").reverse().join("");
    while (bn.length < 32)
        bn += '0';
    return parseInt(bn, 2);
};
