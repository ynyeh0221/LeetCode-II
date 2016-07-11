class Solution {
public:
    int climbStairs(int n) {
        if (n == 1 || n == 2)
            return n;
        int pre1 = 1, pre2 = 2;
        for (int i = 3; i <= n; i++)
        {
            int temp = pre2;
            pre2 = pre1 + pre2;
            pre1 = temp;
        }
        return pre2;
    }
};
