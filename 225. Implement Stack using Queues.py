class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q1 = []
        self.q2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.q1 += [x]

    def pop(self):
        """
        :rtype: nothing
        """
        while len(self.q1)>1:
            self.q2 += [self.q1.pop(0)]
        self.q1.pop(0)
        while self.q2:
            self.q1 += [self.q2.pop(0)]

    def top(self):
        """
        :rtype: int
        """
        while len(self.q1)>1:
            self.q2 += [self.q1.pop(0)]
        temp = self.q1.pop(0)
        self.q2 += [temp]
        while self.q2:
            self.q1 += [self.q2.pop(0)]
        return temp

    def empty(self):
        """
        :rtype: bool
        """
        return False if self.q1 else True
