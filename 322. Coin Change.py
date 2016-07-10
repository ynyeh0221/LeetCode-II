class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        T = [-1 for i in xrange(amount+1)]
        T[0] = 0
        for a in xrange(amount+1):
            temp = amount + 1
            for c in coins:
                if c <= a and T[a-c] >= 0:
                    temp = min(temp, 1 + T[a-c])
            if temp < amount + 1:
                T[a] = temp
        return T[amount]
