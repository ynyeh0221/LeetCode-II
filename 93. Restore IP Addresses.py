class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        self.DFS(res, 0, [], s)
        return res
        
    def DFS(self, res, start, path, s):
        if len(path) == 4:
            if start == len(s):
                res += ['.'.join(path)]
            return
        for l in xrange(1, 4):
            if start + l > len(s) or (l > 1 and s[start] == '0') or int(s[start: start+l]) > 255 or len(s) - start < 4 - len(path) or len(s) - start > 3 * (4 - len(path)):
                break
            self.DFS(res, start+l, path + [s[start:start+l]], s)
