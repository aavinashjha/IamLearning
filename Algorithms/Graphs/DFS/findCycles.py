"""
findCycles in undirected graph: using backedge
Backedge connects vertex to its ancestor
(Should not be direct parent)
  Y
  |
  |
  X
  parent(X) != Y (it is ancestor other than parent hence is a back edge)
"""
from collections import defaultdict

DISCOVERED=1
EXPLORED=2
# Undiscovered is not in list

class Stack:
    def __init__(self):
        self.s = list()
    def push(self, x):
        self.s.append(x)
    def pop(self):
        return self.s.pop()
    def isEmpty(self):
        return len(self.s) == 0

class Graph:
    def __init__(self, directed=False):
        self.g = defaultdict(list)
        self.directed = directed

    def edge(self, u, v):
        self.g[u].append(v)
        if not self.directed: self.g[v].append(u)

    def neighbors(self, u):
        return self.g[u]

    def dfs(self, u, state, parent):
        """
        As we are encountering edge, we see if the current vertex's(u) parent
        is not v, if its parent its normal tree edge otherwise its backedge
        """
        def processEdge(u, v):
            if parent[u] != v: # ancestor - back edge
                return True

        state[u] = DISCOVERED
        for v in self.neighbors(u):
            if v not in state: # UNDISCOVERED
                parent[v] = u
                if self.dfs(v, state, parent): return True

            elif state[v] != EXPLORED: # Discovered but not explored
                if processEdge(u, v): return True

        state[u] = EXPLORED

        return False

    def hasCycle(self):
        state, parent = dict(), dict()
        for u in self.g.keys():
            if u not in state:
                parent[u] = None
                if self.dfs(u, state, parent):
                    return True
        return False

    def __str__(self):
        graph = []
        for u in self.g.keys():
            for v in self.g[u]:
                graph.append('{}->{}'.format(u, v))
        return ', '.join(graph)

g = Graph()
g.edge(1, 2)
g.edge(2, 4)
g.edge(4, 5)
g.edge(5, 3)
g.edge(3, 1)
print(g)
print(g.hasCycle())

g = Graph()
g.edge(1, 2)
g.edge(2, 4)
print(g)
print(g.hasCycle())

g = Graph(directed=True)
g.edge(0, 1)
g.edge(0, 2)
g.edge(1, 2)
g.edge(2, 0)
g.edge(2, 3)
g.edge(3, 3)
print(g)
print(g.hasCycle())

g = Graph(directed=True)
g.edge(0, 1)
g.edge(0, 2)
g.edge(1, 2)
g.edge(2, 3)
print(g)
print(g.hasCycle())
