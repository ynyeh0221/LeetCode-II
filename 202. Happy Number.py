class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        dic = {}
        temp = tuple(str(n))
        dic[temp] = 1
        while True:
            s = sum([int(i)**2 for i in temp])
            if s == 1:
                return True
            temp = tuple(str(s))
            if temp in dic:
                return False
            dic[temp] = 1
