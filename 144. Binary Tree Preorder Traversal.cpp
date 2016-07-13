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
    vector<int> preorderTraversal(TreeNode* root) {
        if (root == NULL)
            return {};
        stack <TreeNode*> stack;
        stack.push(root);
        vector <int> res {root->val};
        while (!stack.empty())
        {
            while (root != NULL && root->left != NULL)
            {
                stack.push(root->left);
                root = root->left;
                res.push_back(root->val);
            }
            root = stack.top();
            stack.pop();
            if (root->right)
                stack.push(root->right);
            root = root->right;
            if (root != NULL)
                res.push_back(root->val);
        }
        return res;
    }
};
