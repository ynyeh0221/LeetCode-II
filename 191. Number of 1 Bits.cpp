class Solution {
public:
    int hammingWeight(uint32_t n) {
        string s = bitset <32> (n).to_string();
        int res = 0;
        for (int i = 0; i < s.size(); i++)
            res += s[i] - '0';
        return res;
    }
};
