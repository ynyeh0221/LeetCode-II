/**
 * @param {character[][]} board
 * @return {void} Do not return anything, modify board in-place instead.
 */
var solve = function(board) {
    var BFS = function(i, j)
    {
        let queue = [{i: i, j: j}];
        while (queue.length > 0)
        {
            let temp = queue.shift();
            let x = temp.i, y = temp.j;
            if (x < 0 || x >= board.length || y < 0 || y >= board[0].length || board[x][y] != 'O')
                continue;
            board[x][y] = '*';
            queue.push({i: x-1, j: y});
            queue.push({i: x+1, j: y});
            queue.push({i: x, j: y-1});
            queue.push({i: x, j: y+1});
        }
    };
    if (board.length > 0)
    {
        for (let i = 0; i < board.length; i++)
        {
            BFS(i, 0);
            BFS(i, board[0].length-1);
        }
        for (let j = 0; j < board[0].length; j++)
        {
            BFS(0, j);
            BFS(board.length-1, j);
        }
        for (let i = 0; i < board.length; i++)
        {
            for (let j = 0; j < board[0].length; j++)
            {
                if (board[i][j] == 'O')
                    board[i][j] = 'X';
                else if (board[i][j] == '*')
                    board[i][j] = 'O';
            }
        }
    }
};
