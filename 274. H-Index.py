class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        if n == 0 or all(x == 0 for x in citations):
            return 0
        citations = sorted(citations)
        for i in xrange(n):
            if n-i <= citations[i]:
                return n-i
