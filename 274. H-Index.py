class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        citations = sorted(citations)
        for i in xrange(n):
            if n-i <= citations[i]:
                return n-i
        return 0
