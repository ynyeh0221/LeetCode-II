/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int maxDepth(TreeNode* root) {
        if (root == NULL)
            return 0;
        if (root->left == NULL && root->right == NULL)
            return 1;
        int l = maxDepth(root->left), r = maxDepth(root->right);
        return l > r ? l+1 : r+1;
    }
};
