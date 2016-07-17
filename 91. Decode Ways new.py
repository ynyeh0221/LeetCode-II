class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0 or s[0] == '0':
            return 0
        T = [0 for i in xrange(len(s)+1)]
        T[0] = 1
        T[1] = 1
        for i in xrange(2, len(s)+1):
            if s[i-1] == '0':
                if s[i-2] != '0' and int(s[i-2:i]) <= 26:
                    T[i] += T[i-2]
                else:
                    return 0
            else:
                T[i] += T[i-1]
                if s[i-2] != '0' and int(s[i-2:i]) <= 26:
                    T[i] += T[i-2]
        return T[len(s)]
