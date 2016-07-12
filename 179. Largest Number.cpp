class Solution {
public:
    struct {
        bool operator()(string a, string b)
        {   
            return a+b > b+a;
        }
    } compare;
    string largestNumber(vector<int>& nums) {
        vector <string> s;
        for (int i = 0; i < nums.size(); i++)
            s.push_back(to_string(nums[i]));
        sort(s.begin(), s.end(), compare);
        string res = "";
        for (int i = 0; i < s.size(); i++)
            res += s[i];
        return res[0] == '0' ? "0" : res;
    }
};
