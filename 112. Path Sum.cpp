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
    bool DFS(TreeNode* root, int sum)
    {
        if (root == NULL) return false;
        if (root->left == NULL && root->right == NULL && root->val == sum) return true;
        return DFS(root->left, sum - root->val) || DFS(root->right, sum - root->val);
    }
    bool hasPathSum(TreeNode* root, int sum) {
        return DFS(root, sum);
    }
};
