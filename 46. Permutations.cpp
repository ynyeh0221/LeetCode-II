class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector <int> visited (nums.size(), false);
        vector<vector<int>> res;
        DFS(res, {}, nums, visited);
        return res;
    }
    void DFS(vector<vector<int>>& res, vector<int> path, vector<int>& nums, vector<int> visited)
    {
        if (path.size() == nums.size())
        {
            res.push_back(path);
            return;
        }
        for (int i = 0; i < nums.size(); i++)
        {
            if (!visited[i])
            {
                visited[i] = true;
                path.push_back(nums[i]);
                DFS(res, path, nums, visited);
                path.pop_back();
                visited[i] = false;
            }
        }
    }
};
