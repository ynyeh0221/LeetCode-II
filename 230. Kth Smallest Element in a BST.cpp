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
    int kthSmallest(TreeNode* root, int k) {
        stack <TreeNode*> s;
        s.push(root);
        while (!s.empty())
        {
            while (root != NULL && root->left != NULL)
            {
                s.push(root->left);
                root = root->left;
            }
            root = s.top();
            s.pop();
            if (--k == 0)
                return root->val;
            if (root->right)
                s.push(root->right);
            root = root->right;
        }
        return 0;
    }
};
