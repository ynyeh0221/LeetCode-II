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
    int sumNumbers(TreeNode* root) {
        int res = 0;
        preorder(res, 0, root);
        return res;
    }
    void preorder(int& res, int s, TreeNode* root)
    {
        if (root == NULL)
            return;
        if (root->left == NULL && root->right == NULL)
        {
            res += 10*s + root->val;
            return;
        }
        preorder(res, 10*s + root->val, root->left);
        preorder(res, 10*s + root->val, root->right);
    }
};
