class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        en = 1
        for i in xrange(len(digits)-1, -1, -1):
            temp = digits[i] + en
            if temp < 10:
                digits[i] = temp
                return digits
            else:
                digits[i] = temp - 10
        return [1] + digits
