class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        int en = 1;
        for (int i = digits.size()-1; i >= 0; i--)
        {
            int temp = digits[i] + en;
            if (temp < 10)
            {
                digits[i] = temp;
                return digits;
            }
            else
                digits[i] = temp - 10;
        }
        digits.insert(digits.begin(), 1);
        return digits;
    }
};
