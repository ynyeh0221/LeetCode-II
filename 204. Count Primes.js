/**
 * @param {number} n
 * @return {number}
 */
var countPrimes = function(n) {
    if (n === 0 || n === 1) return 0;
    var T = [];
    for (var i = 0; i < n; i++)
    {
        if (i === 0 || i === 1)
            T.push(0);
        else
            T.push(1);
    }
    for (i = 2; i*i <= n; i++)
    {
        for (var j = i; j < n; j += i)
        {
            if (T[j] == 1 && i != j)
                T[j] = 0;
        }
    }
    var res = 0;
    for (i = 0; i < n; i++)
        res += T[i];
    return res;
};
