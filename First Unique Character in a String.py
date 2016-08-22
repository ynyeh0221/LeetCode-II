class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        for i in s:
            if i not in dic:
                dic[i] = 0
            dic[i] += 1
        for i in xrange(len(s)):
            if dic[s[i]] == 1:
                return i
        return -1
