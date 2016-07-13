class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_to_t = {}
        t_to_s = {}
        for i in xrange(len(s)):
            if s[i] not in s_to_t and t[i] not in t_to_s:
                s_to_t[s[i]] = t[i]
                t_to_s[t[i]] = s[i]
            elif not (s[i] in s_to_t and t[i] in t_to_s and s_to_t[s[i]] == t[i] and t_to_s[t[i]] == s[i]):
                return False
        return True
