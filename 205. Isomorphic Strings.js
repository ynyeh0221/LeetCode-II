/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isIsomorphic = function(s, t) {
    let s_to_t = {}, t_to_s = {};
    for (let i = 0; i < s.length; i++)
    {
        if (!(s[i] in s_to_t) && !(t[i] in t_to_s))
        {
            s_to_t[s[i]] = t[i];
            t_to_s[t[i]] = s[i];
        }
        else if (!(s[i] in s_to_t && t[i] in t_to_s && s_to_t[s[i]] == t[i] && t_to_s[t[i]] == s[i]))
            return false;
    }
    return true;
};
