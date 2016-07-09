class Solution {
public:
    string reverseString(string s) {
        string res = "";
        for (string::reverse_iterator rit=s.rbegin(); rit!=s.rend(); ++rit)
            res += *rit;
        return res;
    }
};
