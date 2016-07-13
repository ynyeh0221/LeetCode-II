class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        res = 0
        visited = [[False for j in xrange(len(grid[0]))] for i in xrange(len(grid))]
        for i in xrange(len(grid)):
            for j in xrange(len(grid[0])):
                if not visited[i][j] and grid[i][j] == '1':
                    self.count(i, j, grid, visited)
                    res += 1
        return res
        
    def count(self, i, j, grid, visited):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or visited[i][j] or grid[i][j] == '0':
            return
        visited[i][j] = True
        self.count(i-1, j, grid, visited)
        self.count(i+1, j, grid, visited)
        self.count(i, j-1, grid, visited)
        self.count(i, j+1, grid, visited)
