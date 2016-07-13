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
var isValidBST = function(root) {
    let res = true;
    var inorder = function(root, nums)
    {
        if (root === null)
            return;
        if (res)
        {
            inorder(root.left, nums);
            if (nums.length === 0 || (nums.length > 0 && root.val > nums[nums.length-1]))
                nums.push(root.val);
            else
                res = false;
            inorder(root.right, nums);
        }
    };
    inorder(root, []);
    return res;
};
