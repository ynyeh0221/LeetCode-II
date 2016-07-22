class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        res = ""
        for j in xrange(len(strs[0])):
            for i in xrange(len(strs)):
                if j >= len(strs[i]) or strs[i][j] != strs[0][j]:
                    return res
            res += strs[0][j]
        return res
