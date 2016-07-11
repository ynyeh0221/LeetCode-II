class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        freq_s, freq_t = [0 for i in xrange(26)], [0 for i in xrange(26)]
        for i in xrange(len(s)):
            freq_s[ord(s[i]) - ord('a')] += 1
            freq_t[ord(t[i]) - ord('a')] += 1
        return True if freq_s == freq_t else False
