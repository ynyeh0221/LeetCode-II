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
 * @return {boolean}
 */
var hasPathSum = function(root, sum) {
    return DFS(root, sum);
};

var DFS = function(root, sum) {
    if (root === null)
        return false;
    if (root.left === null && root.right === null && root.val == sum)
        return true;
    return DFS(root.left, sum - root.val) || DFS(root.right, sum - root.val);
};
