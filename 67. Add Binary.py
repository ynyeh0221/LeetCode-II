class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = ""
        en = 0
        n = min(len(a), len(b))
        for i in xrange(n):
            temp = int(a[len(a)-1-i]) + int(b[len(b)-1-i]) + en
            if temp < 2:
                res = str(temp) + res
                en = 0
            else:
                res = str(temp - 2) + res
                en = 1
        if len(b) == n:
            for i in xrange(len(a)-n-1, -1, -1):
                temp = int(a[i]) + en
                if temp < 2:
                    res = str(temp) + res
                    en = 0
                else:
                    res = str(temp - 2) + res
                    en = 1
        if len(a) == n:
            for i in xrange(len(b)-n-1, -1, -1):
                temp = int(b[i]) + en
                if temp < 2:
                    res = str(temp) + res
                    en = 0
                else:
                    res = str(temp - 2) + res
                    en = 1
        if en == 1:
            res = '1' + res
        return res
