/**
 * @param {number} n
 * @return {string}
 */
var countAndSay = function(n) {
    let res = "1";
    for (let i = 2; i <= n; i++)
    {
        temp = "";
        count = 1;
        for (let j = 1; j < res.length; j++)
        {
            if (res[j] != res[j-1])
            {
                temp += count.toString() + res[j-1];
                count = 0;
            }
            count += 1;
        }
        temp += count.toString() + res[res.length-1];
        res = temp;
    }
    return res;
};
