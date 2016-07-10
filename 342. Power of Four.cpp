class Solution {
public:
    bool isPowerOfFour(int num) {
        if (num <= 0) return false;
        float temp = log10(num) / log10(4);
        return (int) temp == temp ? true : false;
    }
};
