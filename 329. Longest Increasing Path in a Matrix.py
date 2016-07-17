# timeout

class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix:
            return 0
        self.matrix = matrix
        self.n = len(matrix)
        self.m = len(matrix[0])
        self.res = 0
        for i in xrange(self.n):
            for j in xrange(self.m):
                visited = [[False for k in xrange(self.m)] for l in xrange(self.n)]
                self.find(i, j, 0, -sys.maxint, visited)
        return self.res
        
    def find(self, i, j, length, last, visited):
        if i < 0 or j < 0 or i >= self.n or j >= self.m or self.matrix[i][j] <= last or visited[i][j]:
            self.res = max(self.res, length)
            return
        visited[i][j] = True
        self.find(i-1, j, length + 1, self.matrix[i][j], visited)
        self.find(i+1, j, length + 1, self.matrix[i][j], visited)
        self.find(i, j-1, length + 1, self.matrix[i][j], visited)
        self.find(i, j+1, length + 1, self.matrix[i][j], visited)
        visited[i][j] = False
