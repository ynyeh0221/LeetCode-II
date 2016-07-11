class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for i in s:
            if i == '(' or i == '[' or i == '{':
                stack += [i]
            else:
                if i == ')':
                    if not stack or (stack and stack.pop() != '('):
                        return False
                elif i == ']':
                    if not stack or (stack and stack.pop() != '['):
                        return False
                elif i == '}':
                    if not stack or (stack and stack.pop() != '{'):
                        return False
        return True if not stack else False
