class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size())
            return false;
        vector <int> freq_s (26), freq_t (26);
        for (int i = 0; i < s.size(); i++)
        {
            freq_s[s[i] - 'a'] += 1;
            freq_t[t[i] - 'a'] += 1;
        }
        return freq_s == freq_t ? true :false;
    }
};
