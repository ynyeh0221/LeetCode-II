class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return []
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 0
            dic[i] += 1
        res = []
        for i in sorted(dic.items(), key = lambda x: -x[1]):
            if len(res) < k:
                res += [i[0]]
            else:
                break
        return res
