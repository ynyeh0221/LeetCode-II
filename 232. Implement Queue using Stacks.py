class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.s1 += [x]

    def pop(self):
        """
        :rtype: nothing
        """
        if self.s2:
            self.s2.pop()
        else:
            while self.s1:
                self.s2 += [self.s1.pop()]
            self.s2.pop()

    def peek(self):
        """
        :rtype: int
        """
        if self.s2:
            return self.s2[len(self.s2)-1]
        else:
            while self.s1:
                self.s2 += [self.s1.pop()]
            return self.s2[len(self.s2)-1]

    def empty(self):
        """
        :rtype: bool
        """
        return True if not self.s1 and not self.s2 else False
