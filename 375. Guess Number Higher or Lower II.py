class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        T = [[0 for j in range(n + 1)] for i in range(n + 1)]
        return self.find(T, 1, n)
 
    def find(self, T, l, r):
        if l >= r:
            return 0
        if T[l][r]:
            return T[l][r]
        T[l][r] = min(i + max(self.find(T, l, i - 1), self.find(T, i + 1, r)) for i in xrange(l, r + 1))
        return T[l][r]
