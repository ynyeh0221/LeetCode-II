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
var preorderTraversal = function(root) {
    if (root === null)
        return [];
    let stack = [root], res = [];
    res.push(root.val);
    while (stack.length > 0)
    {
        while (root !== null && root.left !== null)
        {
            stack.push(root.left);
            root = root.left;
            res.push(root.val);
        }
        root = stack.pop();
        if (root !== null && root.right !== null)
            stack.push(root.right);
        root = root.right;
        if (root !== null)
            res.push(root.val);
    }
    return res;
};
