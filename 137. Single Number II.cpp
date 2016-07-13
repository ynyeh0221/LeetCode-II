class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int one=0, two=0;
        for(int i = 0; i < nums.size(); i++)
        {
            two = two | (one & nums[i]);
            one = one ^ nums[i];
            int three = two & one;
            two ^= three;
            one ^= three;
        }
        return one|two;
    }
};
