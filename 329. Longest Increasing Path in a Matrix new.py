class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix:
            return 0
        n = len(matrix)
        m = len(matrix[0])
        res = 0
        T = [[0 for j in xrange(m)] for i in xrange(n)]
        for i in xrange(n):
            for j in xrange(m):
                res = max(res, self.DFS(i, j, n, m, matrix, T))
        return res
        
    def DFS(self, x, y, n, m, matrix, T):
        if T[x][y] > 0:
            return T[x][y]
        for dx, dy in ([(1, 0), (-1, 0), (0, 1), (0, -1)]):
            nx = x + dx
            ny = y + dy
            if nx >= 0 and ny >= 0 and nx < n and ny < m and matrix[nx][ny] > matrix[x][y]:
                T[x][y] = max(T[x][y], self.DFS(nx, ny, n, m, matrix, T))
        T[x][y] += 1
        return T[x][y]
