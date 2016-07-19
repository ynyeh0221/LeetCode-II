# timeout

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        start = 0
        end = len(height)-1
        res = 0
        maxh = max([l for l in height])
        for j in xrange(1, maxh+1):
            flag = 0
            for k in xrange(end+1):
                if flag == 0 and height[k] > j-1:
                    start = k
                    flag = 1
                if flag == 1 and height[k] > j-1:
                    end = k
            i = start
            while i <= end:
                if j - height[i] > 0:
                    res += j - height[i]
                    height[i] += 1
                i += 1
        return res
