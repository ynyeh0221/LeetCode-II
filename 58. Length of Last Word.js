/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    s = s.trim();
    for (let i = s.length-1; i >= 0; i--)
    {
        if (s[i] == ' ')
            return s.length - i - 1;
        if (i === 0)
            return s.length - i;
    }
    return 0;
};
