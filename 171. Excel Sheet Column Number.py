class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for i in s:
            res = res  * 26 + ord(i) - ord('A') + 1
        return res
