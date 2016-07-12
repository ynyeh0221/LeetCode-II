/**
 * @param {number} n
 * @return {number[]}
 */
var grayCode = function(n) {
    let res = [0];
    for (let i = 0; i < n; i++)
    {
        let temp = [];
        for (let j = 0; j < res.length; j++)
            temp.push(res[j] + Math.pow(2, i));
        res = res.concat(temp.reverse());
    }
    return res;
};
