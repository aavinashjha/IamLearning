"""
findPath from a vertex to another vertex
- This is the minimum path if we use Breadth First Traversal
"""
from collections import defaultdict

class Graph:
    def __init__(self):
        self.g = defaultdict(list)

    def edge(self, u, v):
        # Considering undirected graph
        self.g[u].append(v)
        self.g[v].append(u)

    def neighbors(self, u):
        return self.g[u]

    def bfs(self, s):
        level, parent, currLevel = {}, {}, 1
        level[s], parent[s] = currLevel, None

        frontier = [s]
        while frontier:
            nextLevel = []
            for u in frontier:
                for v in self.neighbors(u):
                    if v not in level:
                        parent[v] = u
                        level[v] = currLevel
                        nextLevel.append(v)

            currLevel += 1
            frontier = nextLevel
        return level, parent

    def findPath(self, u, v):
        path = []
        _, parent = self.bfs(u)

        while v:
            path.append(v)
            v = parent[v]
        return path[::-1]

g = Graph()
g.edge(1, 2)
g.edge(2, 3)
g.edge(3, 4)
g.edge(4, 5)
g.edge(5, 1)
g.edge(1, 6)
g.edge(2, 5)

print(g.findPath(1, 4))
