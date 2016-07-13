/**
 * @param {character[][]} grid
 * @return {number}
 */
var numIslands = function(grid) {
    let res = 0;
    let visited = [];
    for (let i = 0; i < grid.length; i++)
    {
        visited.push([]);
        for (let j = 0; j < grid[0].length; j++)
            visited[visited.length-1].push(false);
    }
    var count = function(i, j)
    {
        if (i < 0 || i >= grid.length || j < 0 || j >= grid[0].length || visited[i][j] || grid[i][j] == '0')
            return;
        visited[i][j] = true;
        count(i-1, j);
        count(i+1, j);
        count(i, j-1);
        count(i, j+1);
    };
    for (let i = 0; i < grid.length; i++)
    {
        for (let j = 0; j < grid[0].length; j++)
        {
            if (!visited[i][j] && grid[i][j] == '1')
            {
                count(i, j);
                res += 1;
            }
        }
    }
    return res;
};
