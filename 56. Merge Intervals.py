# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0 or len(intervals) == 1:
            return intervals
        intervals = sorted(intervals, key = lambda x: x.start)
        res = [intervals[0]]
        for i in xrange(len(intervals)):
            if intervals[i].start <= res[len(res)-1].end:
                res[len(res)-1].end = max(res[len(res)-1].end, intervals[i].end)
            else:
                 res += [intervals[i]]
        return res
