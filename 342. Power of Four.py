import math
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        temp = math.log10(num) / float(math.log10(4))
        return True if int(temp) == temp else False
