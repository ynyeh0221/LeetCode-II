class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        visited = [[False for j in xrange(len(board[0]))] for i in xrange(len(board))]
        self.res = False
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if board[i][j] == word[0]:
                    self.dfs(i, j, 0, board, word, visited)
        return self.res
    
    def dfs(self, i, j, ind, board, word, visited):
        if ind == len(word):
            self.res = True
            return
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or visited[i][j] or board[i][j] != word[ind]:
            return
        if not self.res:
            visited[i][j] = True
            self.dfs(i-1, j, ind+1, board, word, visited)
            self.dfs(i+1, j, ind+1, board, word, visited)
            self.dfs(i, j-1, ind+1, board, word, visited)
            self.dfs(i, j+1, ind+1, board, word, visited)
            visited[i][j] = False
