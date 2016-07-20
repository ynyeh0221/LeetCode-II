class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        p_to_s = {}
        s_to_p = {}
        pattern = list(pattern)
        str = str.split(' ')
        if len(str) != len(pattern):
            return False
        for i in xrange(len(pattern)):
            if pattern[i] not in p_to_s and str[i] not in s_to_p:
                p_to_s[pattern[i]] = str[i]
                s_to_p[str[i]] = pattern[i]
            elif not (pattern[i] in p_to_s and str[i] in s_to_p and p_to_s[pattern[i]] == str[i] and s_to_p[str[i]] == pattern[i]):
                return False
        return True
