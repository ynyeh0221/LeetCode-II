class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        if not envelopes:
            return 0
        envelopes = sorted(envelopes, key = lambda x: (x[0], -x[1]))
        T = [1 for i in xrange(len(envelopes))]
        g = [sys.maxint for i in xrange(len(envelopes)+1)]
        res = 0
        for i in xrange(len(envelopes)):
            k = self.lower_bound(g, 1, len(envelopes), envelopes[i][1])
            T[i] = k
            g[k] = envelopes[i][1]
            res = max(res, T[i])
        return res
    
    def lower_bound(self, arr, l, r, x):
        while l < r:
            mid = (l + r) >> 1
            if x <= arr[mid]:
                r = mid
            else:
                l = mid + 1
        return l
