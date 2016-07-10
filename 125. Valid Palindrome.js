/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    var l = 0;
    var r = s.length-1;
    var myRegEx  = /[^a-z\d]/i;
    s = s.toLowerCase();
    while (l <= r)
    {
        if (!myRegEx.test(s[l]) && !myRegEx.test(s[r]))
        {
            if (s[l] == s[r])
            {
                l += 1;
                r -= 1;
            }
            else
                return false;
        }
        else if (myRegEx.test(s[l]) && !myRegEx.test(s[r]))
            l += 1;
        else if (!myRegEx.test(s[l]) && myRegEx.test(s[r]))
            r -= 1;
        else
        {
            l += 1;
            r -= 1;
        }
    }
    return true;
};
