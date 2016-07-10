/**
 * @param {number} n
 * @param {number} k
 * @return {number[][]}
 */
var combine = function(n, k) {
    var res = [];
    var DFS = function(path, start, n, k)
    {
        var i;
        if (path.length == k)
        {
            res.push([]);
            for (i = 0; i < path.length; i++)
                res[res.length-1].push(path[i]);
            return;
        }
        for (i = start; i <= n; i++)
        {
            path.push(i);
            DFS(path, i+1, n, k);
            path.pop();
        }
    };
    DFS([],1,n,k);
    return res;
};
