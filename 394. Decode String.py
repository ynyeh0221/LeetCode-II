class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        nums = []
        n = i = 0
        res = ''
        while i < len(s):
            if s[i].isdigit():
                n = 10 * n + int(s[i])
            elif s[i] == ']':
                if n > 0:
                    nums += [n]
                    n = 0
                temp = ''
                while stack[-1] != '[':
                    temp += stack.pop()[::-1]
                stack.pop()
                temp = temp[::-1]
                times = nums.pop()
                for j in xrange(times):
                    stack += [temp]
            else:
                if n > 0:
                    nums += [n]
                    n = 0
                stack += [s[i]]
            i += 1
        return ''.join(stack)
