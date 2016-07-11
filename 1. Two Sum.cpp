class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map <int, int> dic;
        for (int i = 0; i < nums.size(); i++)
            dic[nums[i]] = i;
        for (int i = 0; i < nums.size(); i++)
        {
            if (dic.count(target - nums[i]) > 0 && i < dic[target - nums[i]])
                return {i, dic[target - nums[i]]};
        }
        return {};
    }
};
