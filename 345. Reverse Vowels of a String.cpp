class Solution {
public:
    string reverseVowels(string s) {
        string vowel = "AEIOUaeiou";
        int l = 0, r = s.size()-1;
        while (l <= r)
        {
            size_t foundl = vowel.find(s[l]), foundr = vowel.find(s[r]);
            if (foundl != string::npos && foundr != string::npos)
            {
                char temp = s[l];
                s[l] = s[r];
                s[r] = temp;
                l ++;
                r --;
            }
            else if (foundl == string::npos && foundr != string::npos)
                l ++;
            else if (foundl != string::npos && foundr == string::npos)
                r --;
            else
            {
                l ++;
                r --;
            }
        }
        return s;
    }
};
