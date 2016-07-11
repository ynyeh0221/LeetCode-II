/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */
var rightSideView = function(root) {
    let res = [];
    var helper = function(root, level)
    {
        if (root === null)
            return;
        if (res.length == level)
            res.push(root.val);
        helper(root.right, level+1);
        helper(root.left, level+1);
    };
    helper(root, 0);
    return res;
};
