class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        flag = 0
        if n < 0:
            n = -n
            flag = 1
        res = self.power(x, n)
        return res if flag == 0 else 1/float(res)
        
    def power(self, x, n):
        if n == 0:
            return 1
        if n % 2 == 0:
            temp = self.power(x, n/2)
            return temp * temp
        else:
            temp = self.power(x, n/2)
            return x * temp * temp
