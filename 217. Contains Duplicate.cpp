#include <unordered_map>
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_map <int, int> dic;
        for (int i = 0; i < nums.size(); i++)
        {
            if (dic.count(nums[i]) == 0)
                dic[nums[i]] = 1;
            else
                return true;
        }
        return false;
    }
};
