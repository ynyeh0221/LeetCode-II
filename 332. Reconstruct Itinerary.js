/**
 * @param {string[][]} tickets
 * @return {string[]}
 */
var findItinerary = function(tickets) {
    let from_to = {}, visited = {};
    for (let i = 0; i < tickets.length; i++)
    {
        let start = tickets[i][0], end = tickets[i][1];
        if (!(start in from_to))
        {
            from_to[start] = [];
            visited[start] = [];
        }
        from_to[start].push(end);
        visited[start].push(false);
    }
    for (let start in from_to)
        from_to[start] = from_to[start].sort();
    
    let res = [];
    var DFS = function(path, start, visited)
    {
        if (path.length == tickets.length + 1)
        {
            for (let i = 0; i < path.length; i++)
                res.push(path[i]);
            return;
        }
        if (res.length === 0 && start in from_to)
        {
            for (let e = 0; e < from_to[start].length; e++)
            {
                if (!visited[start][e])
                {
                    visited[start][e] = true;
                    path.push(from_to[start][e]);
                    DFS(path, from_to[start][e], visited);
                    path.pop();
                    visited[start][e] = false;
                }
            }
        }
    };
    DFS(['JFK'], 'JFK', visited);
    return res;
};
