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
private:
    bool res = true;
public:
    bool isValidBST(TreeNode* root) {
        vector <int> nums;
        inorder(root, nums);
        return res;
    }
    
    void inorder(TreeNode* root, vector <int>& nums)
    {
        if (root == NULL)
            return;
        if (res)
        {
            inorder(root->left, nums);
            if (nums.size() == 0 || (nums.size() > 0 && root->val > nums[nums.size() - 1]))
                nums.push_back(root->val);
            else
                res = false;
            inorder(root->right, nums);
        }
    }
};
