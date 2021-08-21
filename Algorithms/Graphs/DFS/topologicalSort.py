"""
Topological Sort of graph is an ordering on vertices so that all edges go from left to right
DAGs have atleast one topological sort
Directed graph is a DAG if and only if no backedges are encountered during a depth first search
Labelling each of the vertices in reverse order that they are marked processed finds a topological sort of DAG 
Leftmost node has to have indegreee of 0
"""
class Stack:
    def __init__(self):
        self.s = list()

    def push(self, x):
        self.s.append(x)

    def pop(self):
        return self.s.pop()

    def isEmpty(self):
        return len(self.s) == 0

from collections import defaultdict
class Graph:
    def __init__(self):
        self.g = defaultdict(list)
        #self.exitTime = dict()
        self.discovered = set()
        #self.time = 0

    def edge(self, u, v):
        self.g[u].append(v)

    def neighbors(self, u):
        return self.g[u]

    def _dfs(self, u, s):
        def processVertexEarly(u):
            self.discovered.add(u)
            #self.time += 1

        def processVertexLate(u):
            #self.time += 1
            #self.exitTime[u] = self.time
            s.push(u)
            

        processVertexEarly(u)
        for v in self.neighbors(u):
            if v not in self.discovered:
                self._dfs(v, s)
        processVertexLate(u)

    def topologicalSort(self):
        s = Stack()
        for u in self.g.keys():
            if u not in self.discovered:
                self._dfs(u, s)
        #return [i[0] for i in sorted(self.exitTime.items(), key=lambda x: x[1])][::-1]

        topSort = list()
        while not s.isEmpty():
            topSort.append(s.pop())
        return topSort


g = Graph()
g.edge('A', 'B')
g.edge('A', 'C')
g.edge('B', 'C')
g.edge('B', 'D')
g.edge('C', 'E')
g.edge('C', 'F')
g.edge('E', 'D')
g.edge('F', 'E')
g.edge('G', 'A')
g.edge('G', 'F')
print(g.topologicalSort())
