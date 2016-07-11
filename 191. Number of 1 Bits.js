/**
 * @param {number} n - a positive integer
 * @return {number}
 */
var hammingWeight = function(n) {
    let s = (n >>> 0).toString(2);
    let res = 0;
    for (let i = 0; i < s.length; i++)
    {
        if (s[i] == '1')
            res += 1;
    }
    return res;
};
