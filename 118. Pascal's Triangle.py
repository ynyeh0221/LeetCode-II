class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]
        res = [[1],[1,1]]
        for i in xrange(3, numRows+1):
            res += [[1] + [res[len(res)-1][i-1] + res[len(res)-1][i] for i in xrange(1, len(res[len(res)-1]))] +[1]]
        return res
