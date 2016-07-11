/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    if (s.length != t.length)
        return false;
    var freq_s = [];
    var freq_t = [];
    for (var i = 0; i < 26; i++)
    {
        freq_s.push(0);
        freq_t.push(0);
    }
    for (i = 0; i < s.length; i++)
    {
        freq_s[s[i].charCodeAt(0) - 'a'.charCodeAt(0)] += 1;
        freq_t[t[i].charCodeAt(0) - 'a'.charCodeAt(0)] += 1;
    }
    for (i = 0; i < 26; i++)
    {
        if (freq_s[i] != freq_t[i])
            return false;
    }
    return true;
};
