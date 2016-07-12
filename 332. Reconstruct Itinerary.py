class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        self.n = len(tickets)
        from_to = {}
        visited = {}
        for ticket in tickets:
            if ticket[0] not in from_to:
                from_to[ticket[0]] = []
                visited[ticket[0]] = []
            from_to[ticket[0]] += [ticket[1]]
            visited[ticket[0]] += [False]
        for key in from_to.keys():
            from_to[key] = sorted(from_to[key])
        self.res = []
        self.DFS(['JFK'], 'JFK', from_to, visited)
        return self.res
        
    def DFS(self, path, start, from_to, visited):
        if len(path) == self.n + 1:
            self.res = path[:]
            return
        if not self.res and start in from_to:
            for e in xrange(len(from_to[start])):
                if not visited[start][e]:
                    visited[start][e] = True
                    self.DFS(path + [from_to[start][e]], from_to[start][e], from_to, visited)
                    visited[start][e] = False
