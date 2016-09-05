class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == '':
            return True
        if t == '' and s != '':
            return False
        path = []
        for i in xrange(len(t)):
            if t[i] == s[len(path)]:
                path += [t[i]]
            if len(path) == len(s):
                return True
        return False
