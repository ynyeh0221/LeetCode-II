class Solution {
public:
    void sortColors(vector<int>& nums) {
        int n = nums.size();
        int i = 0;
        while (i < n)
        {
            if (nums[i] == 0)
            {
                int temp = nums[i];
                nums.erase(nums.begin() + i);
                nums.insert(nums.begin(), temp);
            }
            else if (nums[i] == 2)
            {
                int temp = nums[i];
                nums.erase(nums.begin() + i);
                nums.push_back(temp);
                i--;
                n--;
            }
            i++;
        }
    }
};
