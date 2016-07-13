class Solution {
public:
    int findMin(vector<int>& nums) {
        int res = nums[0];
        for (int i = 0; i < nums.size(); i++)
        {
            if (nums[i] < res)
                return nums[i];
        }
        return res;
    }
};
