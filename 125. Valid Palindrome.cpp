class Solution {
public:
    bool isPalindrome(string s) {
        int l = 0, r = s.length()-1;
        locale loc;
        for (int i=0; i < s.length(); i++)
            s[i] = tolower(s[i], loc);
        while (l <= r)
        {
            if (isalnum(s[l]) && isalnum(s[r]))
            {
                if (s[l] == s[r])
                {
                    l ++;
                    r --;
                }
                else
                    return false;
            }
            else if (!isalnum(s[l]) && isalnum(s[r]))
                l ++;
            else if (isalnum(s[l]) && !isalnum(s[r]))
                r --;
            else
            {
                l ++;
                r --;
            }
        }
        return true;
    }
};
