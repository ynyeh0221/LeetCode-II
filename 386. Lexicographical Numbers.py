class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        i = 1
        res = []
        stack = []
        while i <= n:
            stack.append(i)
            res.append(i)
            i *= 10
        while stack:
            j = stack.pop()
            if j % 10 != 9:
                j += 1
                while j <= n:
                    stack.append(j)
                    res.append(j)
                    j *= 10
        return res
