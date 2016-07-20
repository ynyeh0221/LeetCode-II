/**
 * @param {character[][]} board
 * @param {string} word
 * @return {boolean}
 */
var exist = function(board, word) {
    let visited = [];
    for (let i = 0; i < board.length; i++)
    {
        visited.push([]);
        for (let j = 0; j < board[0].length; j++)
            visited[visited.length-1].push(false);
    }
    let res = false;
    var dfs = function(i, j, ind, visited)
    {
        if (ind == word.length)
        {
            res = true;
            return;
        }
        if (i < 0 || j < 0 || i >= board.length || j >= board[0].length || visited[i][j] || board[i][j] != word[ind])
            return;
        if (!res)
        {
            visited[i][j] = true;
            dfs(i-1, j, ind+1, visited);
            dfs(i+1, j, ind+1, visited);
            dfs(i, j-1, ind+1, visited);
            dfs(i, j+1, ind+1, visited);
            visited[i][j] = false;
        }
    };
    for (let i = 0; i < board.length; i++)
    {
        for (let j = 0; j < board[0].length; j++)
        {
            if (board[i][j] == word[0])
                dfs(i, j, 0, visited);
        }
    }
    return res;
};
