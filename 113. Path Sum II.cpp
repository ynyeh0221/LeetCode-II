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
    vector<vector<int>> pathSum(TreeNode* root, int sum) {
        vector<vector<int>> res;
        DFS(res, {}, root, sum);
        return res;
    }
    
    void DFS(vector<vector<int>>& res, vector <int> path, TreeNode* root, int sum)
    {
        if (root == NULL)
            return;
        if (root->left == NULL && root->right == NULL && sum == root->val)
        {
            path.push_back(root->val);
            res.push_back(path);
            path.pop_back();
            return;
        }
        path.push_back(root->val);
        DFS(res, path, root->left, sum - root->val);
        DFS(res, path, root->right, sum - root->val);
        path.pop_back();
    }
};
