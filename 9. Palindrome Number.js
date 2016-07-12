/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    if (Math.floor(x / 10) === 0)
        return true;
    if (x < 0 || x % 10 === 0)
        return false;
    let temp = 0;
    while (x > 0)
    {
        temp = 10*temp + x % 10;
        if (temp == x || temp == Math.floor(x / 10))
            return true;
        x = Math.floor(x / 10);
    }
    return false;
};
