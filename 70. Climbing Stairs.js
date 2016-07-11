/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {
    if (n == 1 || n == 2)
        return n;
    let pre1 = 1, pre2 = 2;
    for (let i = 3; i <= n; i++)
    {
        let temp = pre2;
        pre2 = pre1 + pre2;
        pre1 = temp;
    }
    return pre2;
};
