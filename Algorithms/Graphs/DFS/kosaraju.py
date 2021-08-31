"""
Strongly Connected Component: Every vertex in a component is reachable from every other component
- DFS on a graph, note exit time
- Reverse the graph [Stack]
- DFS on reversed graph
- Time: O(M+N) for each step
- Space: O(N)
- 2 pass algorithm
- Each group forms a vertex of DAG
- Atleast one vertex from prior group will be on top of stack 

ABC-->DEF<----GHIJ---->K

"""
from collections import defaultdict
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
    def __init__(self):
        self.g = defaultdict(list)

    def edge(self, u, v):
        self.g[u].append(v)

    def neighbors(self, u):
        return self.g[u]

    def vertices(self):
        return self.g.keys()

    def reverse(self):
        rg = defaultdict(list)
        for u, al in self.g.items():
            for v in al:
                rg[v].append(u)
        self.g = rg

    def dfs(self):
        def processVertexEarly(u):
            discovered.add(u)

        def processVertexLate(u):
            # Adding in opposite order of exit time
            stack.push(u)

        def _dfs(u):
            processVertexEarly(u)
            for v in self.neighbors(u):
                if v not in discovered:
                    _dfs(v)
            processVertexLate(u)

        discovered = set()
        stack = Stack()

        for u in list(self.vertices()):
            if u not in discovered:
                _dfs(u)

        return stack

    def dfs2(self, u, discovered, result):
        result.append(u)
        discovered.add(u)
        for v in self.neighbors(u):
            if v not in discovered:
                self.dfs2(v, discovered, result)

g = Graph()
g.edge('a', 'b')
g.edge('b', 'c')
g.edge('b', 'd')
g.edge('c', 'a')
g.edge('d', 'e')
g.edge('e', 'f')
g.edge('f', 'd')
g.edge('g', 'f')
g.edge('g', 'h')
g.edge('h', 'i')
g.edge('i', 'j')
g.edge('j', 'g')
g.edge('j', 'k')
stack = g.dfs()

g.reverse()

discovered = set()
while not stack.isEmpty():
    result = list()
    u = stack.pop()
    if u in discovered: continue
    g.dfs2(u, discovered, result)
    print(result)



