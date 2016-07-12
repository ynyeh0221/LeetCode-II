/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var permuteUnique = function(nums) {
    let res = [];
    let visited = [];
    for (let i = 0; i < nums.length; i++)
        visited.push(false);
    nums = nums.sort((a,b) => a-b);
    var DFS = function(path, visited)
    {
        if (path.length == nums.length)
        {
            res.push([]);
            for (let i = 0; i < path.length; i++)
                res[res.length-1].push(path[i]);
            return;
        }
        for (let i = 0; i < nums.length; i++)
        {
            if (visited[i] || (i > 0 && nums[i] == nums[i-1] && !visited[i-1]))
                continue;
            visited[i] = true;
            path.push(nums[i]);
            DFS(path, visited);
            path.pop();
            visited[i] = false;
        }
    };
    DFS([], visited);
    return res;
};
