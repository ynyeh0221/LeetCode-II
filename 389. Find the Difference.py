class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dic = {}
        for i in s:
            if i not in dic:
                dic[i] = 0
            dic[i] += 1
        for i in t:
            if i not in dic:
                return i
            else:
                if dic[i] == 0:
                    return i
                dic[i] -= 1
