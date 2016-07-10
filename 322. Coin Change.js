/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */
var coinChange = function(coins, amount) {
    var T = [];
    for (var i = 0; i <= amount; i++)
        T.push(-1);
    T[0] = 0;
    for (var a = 0; a <= amount; a++)
    {
        var temp = amount + 1;
        for (var c = 0; c < coins.length; c++)
        {
            if (coins[c] <= a && T[a-coins[c]] >= 0)
                temp = Math.min(temp, T[a-coins[c]] + 1);
        }
        if (temp < amount + 1)
            T[a] = temp;
    }
    return T[amount];
};
