class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['A','E','I','O','U','a','e','i','o','u']
        l = 0
        r = len(s)-1
        s = list(s)
        while l <= r:
            if s[l] in vowels and s[r] in vowels:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            elif s[l] in vowels and s[r] not in vowels:
                r -= 1
            elif s[l] not in vowels and s[r] in vowels:
                l += 1
            else:
                l += 1
                r -= 1
        return ''.join(s)
