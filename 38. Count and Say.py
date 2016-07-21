class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = "1"
        for i in xrange(2, n+1):
            count = 1
            temp = ""
            for j in xrange(1, len(res)):
                if res[j] != res[j-1]:
                    temp += str(count) + res[j-1]
                    count = 0
                count += 1
            temp += str(count) + res[len(res)-1]
            res = temp
        return res
