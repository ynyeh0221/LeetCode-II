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
var inorderTraversal = function(root) {
    if (root === null)
        return [];
    let stack = [root], res = [];
    while (stack.length > 0)
    {
        while (root !== null && root.left !== null)
        {
            stack.push(root.left);
            root = root.left;
        }
        root = stack.pop();
        res.push(root.val);
        if (root.right)
            stack.push(root.right);
        root = root.right;
    }
    return res;
};
