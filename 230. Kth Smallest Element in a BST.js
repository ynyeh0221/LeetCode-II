/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} k
 * @return {number}
 */
var kthSmallest = function(root, k) {
    let stack = [root];
    while (stack.length > 0)
    {
        while (root && root.left)
        {
            stack.push(root.left);
            root = root.left;
        }
        root = stack.pop();
        k -= 1;
        if (k === 0)
            return root.val;
        if (root.right)
            stack.push(root.right);
        root = root.right;
    }
};
