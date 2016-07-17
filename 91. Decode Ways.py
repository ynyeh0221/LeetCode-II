# timeout

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.res = 0
        self.DFS(0, s)
        return self.res
        
    def DFS(self, start, s):
        if start == len(s):
            self.res += 1
            return 
        for i in xrange(1,3):
            if start+i <= len(s) and s[start] != '0'and int(s[start:start+i]) <= 26:
                self.DFS(start + i, s)
