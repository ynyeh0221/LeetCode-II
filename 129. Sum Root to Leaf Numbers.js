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
var sumNumbers = function(root) {
    var res = 0;
    var preorder = function(s, root) {
        if (root === null)
            return;
        if (root.left === null && root.right === null)
        {
            res += 10*s + root.val;
            return;
        }
        preorder(10*s + root.val, root.left);
        preorder(10*s + root.val, root.right);
    };
    
    preorder(0, root);
    return res;
};
