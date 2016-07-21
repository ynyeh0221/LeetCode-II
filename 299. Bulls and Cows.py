class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        A = B = 0
        dic = {}
        for i in xrange(len(secret)):
            if secret[i] == guess[i]:
                A += 1
            else:
                if secret[i] not in dic:
                    dic[secret[i]] = 0
                dic[secret[i]] += 1
        for i in xrange(len(secret)):
            if secret[i] != guess[i] and guess[i] in dic and dic[guess[i]] > 0:
                B += 1
                dic[guess[i]] -= 1
        return str(A) + 'A' + str(B) + 'B'
