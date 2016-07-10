class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        temp = math.log10(n) / float(math.log10(3))
        return True if int(temp) == temp else False
