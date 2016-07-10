# timeout

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.res = []
        self.DFS([], 1, n, k)
        return self.res
        
    def DFS(self, path, start, n, k):
        if len(path) == k:
            self.res += [path]
            return
        for i in xrange(start, n+1):
            if not path or (path and i > path[len(path)-1]):
                self.DFS(path + [i], start, n, k)
