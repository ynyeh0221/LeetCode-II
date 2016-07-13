class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if len(board) > 0:
            for i in xrange(len(board)):
                self.DFS(i, 0, board)
                self.DFS(i, len(board[0])-1, board)
            for j in xrange(len(board[0])):
                self.DFS(0, j, board)
                self.DFS(len(board)-1, j, board)
            for i in xrange(len(board)):
                for j in xrange(len(board[0])):
                    if board[i][j] == 'O':
                        board[i][j] = 'X'
                    elif board[i][j] == '*':
                        board[i][j] = 'O'
        
    def BFS(self, i, j, board):
        queue = [(i,j)]
        while queue:
            (x, y) = queue.pop(0)
            if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or board[x][y] != 'O':
                continue
            board[x][y] = '*'
            queue += [(x-1, y)]
            queue += [(x+1, y)]
            queue += [(x, y-1)]
            queue += [(x, y+1)]
