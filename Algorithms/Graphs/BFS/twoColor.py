"""
In BFS, we consider all neighbors of a particular vertex
Thatswhy if we select a color for it all its neighbor should be of different color
Whenever we discover a vertex, we will set it to opposite color of its parent
Minimum number of colors required to color graph is NP Complete problem - But upper bound could be found
"""
from collections import defaultdict, deque

UNCOLOURED = 0
WHITE = 1
BLACK = 2

class Queue:
    def __init__(self):
        self.q = deque()
    def enqueue(self, x):
        self.q.append(x)
    def dequeue(self):
        return self.q.popleft()
    def isEmpty(self):
        return len(self.q) == 0
class Graph:
    def __init__(self):
        self.g = defaultdict(list)

    def edge(self, u, v):
        self.g[u].append(v)
        self.g[v].append(u)

    def neighbors(self, u):
        return self.g[u]

    def bfs(self, s, discovered, color):
        q = Queue()
        q.enqueue(s)
        discovered.add(s)

        def processEdge(u, v):
            if color[u] == color[v]:
                print("Not bipartite: {}->{}".format(u, v))
                return False
            color[v] = BLACK if color[u] == WHITE else WHITE
            return True

        while not q.isEmpty():
            u = q.dequeue()
            for v in self.neighbors(u):
                if not processEdge(u, v):
                    return False
                if v not in discovered:
                    discovered.add(v)
                    q.enqueue(v)
        return True

    def bipartite(self):
        discovered, color = set(), [UNCOLOURED]*(len(self.g)+1)
        for u in self.g:
            if u not in discovered:
                color[u] = WHITE
                if not self.bfs(u, discovered, color):
                    return False
        return True

g = Graph()
g.edge(1, 2)
g.edge(1, 3)
g.edge(4, 2)
g.edge(4, 3)
print(g.bipartite())
g = Graph()
g.edge(1, 2)
g.edge(1, 3)
g.edge(2, 3)
print(g.bipartite())
