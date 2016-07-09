class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return 0
        T = [1 for i in xrange(n)]
        T[0] = 0
        T[1] = 0
        for i in xrange(2, n):
            if i*i <= n:
                for j in xrange(i,n,i): # mark all multiples of i as 0 
                    if T[j] == 1 and j != i:
                        T[j] = 0
        return sum(T) # the numbers with T[number] == 1 are primes
