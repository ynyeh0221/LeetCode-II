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
    vector<int> inorderTraversal(TreeNode* root) {
        if (root == NULL)
            return {};
        stack <TreeNode*> stack;
        stack.push(root);
        vector <int> res;
        while (!stack.empty())
        {
            while (root != NULL && root->left != NULL)
            {
                stack.push(root->left);
                root = root->left;
            }
            root = stack.top();
            stack.pop();
            res.push_back(root->val);
            if (root->right)
                stack.push(root->right);
            root = root->right;
        }
        return res;
    }
};
