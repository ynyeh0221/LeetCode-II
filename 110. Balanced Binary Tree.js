/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isBalanced = function(root) {
    var helper = function(root)
    {
        if (root === null)
            return 0;
        if (root.left === null && root.right === null)
            return 1;
        let l = helper(root.left), r = helper(root.right);
        if (l >= 0 && r >= 0)
        {
            if (Math.abs(l - r) > 1)
                return -1;
            return Math.max(l, r) + 1;
        }
    };
    return helper(root) >= 0 ? true : false;
};
