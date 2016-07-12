static inline void rtrim(string &s) {
    s.erase(find_if(s.rbegin(), s.rend(),
        not1(ptr_fun<int, int>(isspace))).base(), s.end());
}

class Solution {
public:
    int lengthOfLastWord(string s) {
        rtrim(s);
        for (int i = s.size()-1; i >= 0; i--)
        {
            if (s[i] == ' ')
                return s.size() - i - 1;
            if (i == 0)
                return s.size() - i;
        }
        return 0;
    }
};
