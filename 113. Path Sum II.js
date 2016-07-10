/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} sum
 * @return {number[][]}
 */
var pathSum = function(root, sum) {
    var res = [];
    var DFS = function(path, root, sum)
    {
        if (root === null)
            return;
        if (root.left === null && root.right === null && sum == root.val)
        {
            path.push(root.val);
            res.push([]);
            for (var i = 0; i < path.length; i++)
                res[res.length-1].push(path[i]);
            path.pop();
            return;
        }
        path.push(root.val);
        DFS(path, root.left, sum - root.val);
        DFS(path, root.right, sum - root.val);
        path.pop();
    };
    DFS([], root, sum);
    return res;
};
