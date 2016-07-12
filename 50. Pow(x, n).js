/**
 * @param {number} x
 * @param {number} n
 * @return {number}
 */
var myPow = function(x, n) {
    let flag = 0;
    if (n < 0)
    {
        n = -n;
        flag = 1;
    }
    var power = function(x, n)
    {
        if (n === 0)
            return 1;
        if (n % 2 === 0)
        {
            let temp = power(x, Math.floor(n/2));
            return temp * temp;
        }
        else
        {
            let temp = power(x, Math.floor(n/2));
            return x * temp * temp;
        }
    };
    let res = power(x, n);
    return flag === 0 ? res : 1/res;
};
