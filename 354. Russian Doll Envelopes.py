# timeout

class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        res = 0
        envelopes = sorted(envelopes, key = lambda x: (x[0],x[1]))
        T = [0 for i in xrange(len(envelopes))]
        for i in xrange(len(envelopes)):
            temp = 1
            for j in xrange(i):
                if envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1]:
                    temp = max(temp, T[j]+1)
            T[i] = temp
            res = max(res, T[i])
        return res
