class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        dic = {}
        res = []
        for i in xrange(len(s)):
            if i + 10 <= len(s):
                if s[i:i+10] not in dic:
                    dic[s[i:i+10]] = 1
                elif dic[s[i:i+10]] == 1:
                    res += [s[i:i+10]]
                    dic[s[i:i+10]] += 1
        return res
