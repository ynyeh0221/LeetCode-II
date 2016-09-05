class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        freq = {}
        for i in s:
            if i not in freq:
                freq[i] = 0
            freq[i] += 1
        f = [x for x in freq if freq[x] < k]
        if not f:
            return len(s)
        seg = re.split('|'.join(f), s)
        return max(self.longestSubstring(l, k) for l in seg)
