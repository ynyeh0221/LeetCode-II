class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        citations = sorted(citations)
        l = 0
        r = n
        while l < r:
            mid = (l+r) >> 1
            if n-mid <= citations[mid]:
                r = mid
            else:
                l = mid + 1
        return n-l
