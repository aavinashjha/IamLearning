from collections import defaultdict
from collections import deque

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

    def __str__(self):
        return "\n".join(["{} -> {}".format(str(k), str(v)) for k, v in self.g.items()])

    def neighbors(self, u):
        return self.g[u]

    def bfsQ(self, s):
        q = Queue()
        q.enqueue(s)
        sol = [s]
        explored = {s}
        
        while not q.isEmpty():
            u = q.dequeue()
            for v in self.neighbors(u):
                if v not in explored:
                    sol.append(v)
                    explored.add(v)
                    q.enqueue(v)
        return sol

    def bfs(self, s):
        level, parent = {}, {}
        level[s], parent[s], currLevel = 0, None, 1 # s is at 0 level and its parent is None
        frontier = [s]
        while frontier:
            nextLevel = []
            for u in frontier:
                for v in self.neighbors(u):
                    if v not in level:
                        level[v] = currLevel
                        parent[v] = u
                        nextLevel.append(v)
            frontier = nextLevel
            currLevel += 1
        return level

g = Graph()
g.edge('s', 'a')
g.edge('s', 'b')
g.edge('a', 'c')
g.edge('b', 'c')
g.edge('b', 'd')
g.edge('c', 'd')
g.edge('c', 'e')
g.edge('e', 'd')
print(g)
print("BFS: {}".format(g.bfs('s')))

print("BFS Queue: {}".format(g.bfsQ('s')))
