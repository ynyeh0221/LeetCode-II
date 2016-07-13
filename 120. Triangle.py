import sys
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        T = [[sys.maxint for j in xrange(len(triangle[i]))] for i in xrange(len(triangle))]
        T[0][0] = triangle[0][0]
        for i in xrange(len(triangle)-1):
            for j in xrange(len(triangle[i])):
                T[i+1][j] = min(T[i+1][j], T[i][j] + triangle[i+1][j])
                T[i+1][j+1] = min(T[i+1][j+1], T[i][j] + triangle[i+1][j+1])
        return min(T[len(triangle)-1])
