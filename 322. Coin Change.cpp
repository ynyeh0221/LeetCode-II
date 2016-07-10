class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        vector <int> T (amount+1, -1);
        T[0] = 0;
        for (int a = 0; a <= amount; a++)
        {
            int temp = amount + 1;
            for (int c = 0; c < coins.size(); c++)
            {
                if (a >= coins[c] && T[a-coins[c]] >= 0)
                    temp = temp < T[a-coins[c]] + 1 ? temp : T[a-coins[c]] + 1;
            }
            if (temp < amount + 1)
                T[a] = temp;
        }
        return T[amount];
    }
};
