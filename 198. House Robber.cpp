class Solution {
public:
    int rob(vector<int>& nums) {
        int n = nums.size();
        if (n == 0)
            return 0;
        else if (n == 1)
            return nums[0];
        else if (n == 2)
            return nums[0] >= nums[1] ? nums[0] : nums[1];
        vector <int> T (n);
        T[0] = nums[0];
        T[1] = nums[0] >= nums[1] ? nums[0] : nums[1];
        for (int i = 2; i < n; i++)
            T[i] = T[i-1] > T[i-2] + nums[i] ? T[i-1] : T[i-2] + nums[i];
        return T[n-1];
    }
};
