class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]
        res = [1,1]
        for i in xrange(2, rowIndex+1):
            res = [1] + [res[i-1] + res[i] for i in xrange(1, len(res))] +[1]
        return res
