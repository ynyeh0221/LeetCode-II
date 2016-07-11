/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {TreeNode}
 */
var invertTree = function(root) {
    var p = root;
    var helper = function(p) {
        if (p === null)
            return [];
        var temp = p.left;
        p.left = p.right;
        p.right = temp;
        helper(p.left);
        helper(p.right);
    };
    helper(p);
    return root;
};
