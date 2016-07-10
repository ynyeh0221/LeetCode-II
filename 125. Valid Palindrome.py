class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        l = 0
        r = len(s)-1
        while l <= r:
            if s[l].isalnum() and s[r].isalnum():
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            elif s[l].isalnum() and not s[r].isalnum():
                r -= 1
            elif not s[l].isalnum() and s[r].isalnum():
                l += 1
            else:
                l += 1
                r -= 1
        return True
