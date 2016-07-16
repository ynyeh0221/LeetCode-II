class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        T = [[0 for j in xrange(len(word2)+1)] for i in xrange(len(word1)+1)]
        for i in xrange(1, len(word1)+1):
            T[i][0] = i
        for j in xrange(1, len(word2)+1):
            T[0][j] = j
        for i in xrange(1, len(word1)+1):
            for j in xrange(1, len(word2)+1):
                diff = 1
                if word1[i-1] == word2[j-1]:
                    diff = 0
                T[i][j] = min(T[i-1][j-1] + diff, T[i-1][j] + 1, T[i][j-1] + 1)
        return T[len(word1)][len(word2)]
