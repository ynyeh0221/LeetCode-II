class Solution {
public:
    bool canJump(vector<int>& nums) {
        int max_achieve = 0;
        for (int i = 0; i < nums.size()-1; i++)
        {
            max_achieve = max_achieve > i + nums[i] ? max_achieve : i + nums[i];
            if (max_achieve < i+1)
                return false;
        }
        return true;
    }
};
