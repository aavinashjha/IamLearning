"""
Find the vertex lying in connected component
"""
from collections import defaultdict, deque
class Queue:
    def __init__(self):
        self.q = deque()
    def enqueue(self, x):
        self.q.append(x)
    def dequeue(self):
        return self.q.popleft()
    def isEmpty(self):
        return len(self.q) == 0
    def __str__(self):
        return "->".join([str(i) for i in self.q])

class Graph:
    def __init__(self):
        self.g = defaultdict(list)
    def edge(self, u, v):
        self.g[u].append(v)
        self.g[v].append(u)
    def neighbors(self, u):
        return self.g[u]

    def bfs(self, s, discovered):
        q = Queue()
        q.enqueue(s)
        discovered.add(s)

        def processVertexEarly(u):
            print("Vertex Discovered: {}".format(u))

        while not q.isEmpty():
            u = q.dequeue()
            processVertexEarly(u)
            for v in self.neighbors(u):
                if v not in discovered:
                   q.enqueue(v)
                   discovered.add(v)

    def connectedComponent(self):
        discovered, c = set(), 0 
        for u in self.g:
            if u not in discovered:
                c += 1
                print("Component: {}".format(c))
                self.bfs(u, discovered)

g = Graph()                
g.edge(1, 3)
g.edge(1, 5)
g.edge(3, 5)
g.edge(5, 7)
g.edge(5, 9)
g.edge(2, 4)
g.edge(6, 8)
g.edge(6, 10)

g.connectedComponent()
