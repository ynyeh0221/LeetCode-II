/**
 * @param {number} n
 * @return {number[]}
 */
var grayCode = function(n) {
    let res = [0];
    for (let i = 0; i < n; i++)
    {
        for (let j = res.length-1; j >= 0; j--)
            res.push(res[j] + Math.pow(2, i));
    }
    return res;
};
