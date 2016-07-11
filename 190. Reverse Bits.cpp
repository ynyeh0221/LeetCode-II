#include <bitset>
class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        string bn = bitset <32> (n).to_string();
        string rbn = "";
        for (string::reverse_iterator rit = bn.rbegin(); rit != bn.rend(); ++rit)
            rbn += *rit;
        uint32_t res = 0;
        for (int i = 0; i < 32; i++)
        {
            if ((rbn[i] - '0') == 1)
                res += pow(2, 31-i); 
        }
        return res;
    }
};
