class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x / 10 == 0:
            return True
        if x < 0 or x % 10 == 0:
            return False
        temp = 0
        while x > 0:
            temp = 10*temp + x % 10
            if x == temp or x / 10 == temp:
                return True
            x /= 10
        return False
