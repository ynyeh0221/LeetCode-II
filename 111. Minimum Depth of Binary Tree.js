/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var minDepth = function(root) {
    if (root === null)
        return 0;
    if (root.left === null && root.right === null)
        return 1;
    let l = minDepth(root.left), r = minDepth(root.right);
    if (l > 0 && r > 0)
        return Math.min(l, r) + 1;
    else
        return l > 0 ? l + 1 : r + 1;
};
