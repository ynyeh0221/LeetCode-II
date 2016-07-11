class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        bn = bin(n)[2:][::-1]
        while len(bn) < 32:
            bn += '0'
        return int(bn, 2)
